import csv
from django.core.management.base import BaseCommand
from property_search.models import FarmProperty
from decimal import Decimal, InvalidOperation

class Command(BaseCommand):
    help = "Seed FarmProperty data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="Path to the CSV file")

    def clean_decimal(self, value):
        if value is None:
            return Decimal("0.00")
        try:
            # Remove commas and strip whitespace
            cleaned = str(value).replace(",", "").strip()
            return Decimal(cleaned)
        except (InvalidOperation, TypeError, ValueError):
            return Decimal("0.00")  # Default fallback


    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                farm = FarmProperty.objects.create(
                    sg_code_21=str(row['sg_code_21']),
                    prop_class=row['min_code'],
                    grv=row['grv'],
                    regdiv=row['regdiv'],
                    farm_name=row['farm_name'],
                    sectional_title=row['sectional_title'],
                    erf_no=row['erf_no'],
                    ptn=row['ptn'],
                    unit=row['unit'],
                    extent=str(row['extent']),
                    ha=str(row['ha']),  
                    physical_address=row['physical_address'],
                    owner=row['owner'],
                    # Ensure this is a valid decimal string for DecimalField
                    market_value=self.clean_decimal(row['market_value']),
                    owner_status=row['owner_status'],
                    category=row['category'],
                    remarks=row.get('remarks', ''),
                )
                count += 1
            self.stdout.write(self.style.SUCCESS(f"Successfully seeded {count} FarmProperty records from {csv_file}"))
