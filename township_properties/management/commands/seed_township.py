import csv
from django.core.management.base import BaseCommand
from township_properties.models import TownshipProperty
from decimal import Decimal, InvalidOperation


class Command(BaseCommand):
    help = "Seed TownshipProperty data from a CSV file"

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
                township = TownshipProperty.objects.create(
                    sg_code_21=str(row['sg_code_21']),
                    prop_class=row['prop_class'],
                    township=row['township'],
                    township_name_ext=row['township_name_ext'],
                    sectional_tittle_name=row['sectional_tittle_name'],
                    erf_no=row['erf_no'],
                    portion_no=row['portion_no'],
                    unit_no=row['unit_no'],
                    registered_owner=row['registered_owner'],
                    street_address=row['street_address'],
                    extent=str(row['extent']),
                    ext=str(row['ext']), 
                    owner_status=row['owner_status'],
                    category=row['category'],
                    market_value=self.clean_decimal(row['market_value']),
                    remarks=row.get('remarks', ''),
                    )
                count += 1
            self.stdout.write(self.style.SUCCESS(f"Successfully seeded {count} TownshipProperty records from {csv_file}"))
