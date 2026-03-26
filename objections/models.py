from django.db import models
from django.conf import settings
import random


#Base Objection Model
class BaseObjection(models.Model):
    # Link to registered user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Objector Information
    OWNER = "owner"
    NOT_OWNER = "not_owner"
    MUNICIPALITY = "municipality"
    AUTHORISED_REP = "auth_representative"

    OBJECTOR_STATUS_CHOICES = [
        (OWNER, "Owner"),
        (NOT_OWNER, "Not Owner"),
        (MUNICIPALITY, "Municipality"),
        (AUTHORISED_REP, "Authorized Representative"),
    ]

    objector_status = models.CharField(max_length=30, choices=OBJECTOR_STATUS_CHOICES)
  
    not_owner_description = models.TextField(null=True, blank=True)

    full_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=50)
    companyreg = models.CharField(max_length=100, null=True, blank=True)
    physical_address = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255, null=True, blank=True)
    phone_home = models.CharField(max_length=20, null=True, blank=True)
    phone_work = models.CharField(max_length=20, null=True, blank=True)
    phone_mobile = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


#Townships Objections
class TownshipObjection(BaseObjection):
    # Link to registered property
    township_property = models.ForeignKey(
        "township_properties.TownshipProperty",
        on_delete=models.CASCADE
    )
    # unique objection number
    objection_number = models.CharField(
        max_length=50,
        unique=True,
        editable=False,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.objection_number:
            self.objection_number = self.generate_objection_number()
        super().save(*args, **kwargs)

    def generate_objection_number(self):
        sg_code = str(self.township_property.sg_code_21)
        last_10 = sg_code[-10:] if len(sg_code) >= 10 else sg_code

        # Find the last objection number for this property
        last_obj = (
            TownshipObjection.objects
            .filter(township_property=self.township_property)
            .exclude(objection_number__isnull=True)
            .order_by("-id")
            .first()
        )

        if last_obj and last_obj.objection_number:
            try:
                # extract the trailing number
                last_num = int(last_obj.objection_number.split("-")[-1])
                next_num = (last_num + 1) % 100
            except ValueError:
                next_num = 0
        else:
            next_num = 0

        return f"ELMGV25-31-{last_10}-{next_num:02d}"


    # Objection Category
    YES = "yes"
    NO = "no"
    BOOLEAN_CHOICES = [(YES, "Yes"), (NO, "No")]

    incorrect_valuation = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO)
    omitted_property = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO)

    # Administrative Query (checkboxes → BooleanFields)
    incorrect_owner_name = models.BooleanField(default=False)
    incorrect_category_rating = models.BooleanField(default=False)
    incorrect_extent = models.BooleanField(default=False)
    incorrect_physical_address = models.BooleanField(default=False)
    incorrect_postal_address = models.BooleanField(default=False)
    rates_query = models.BooleanField(default=False)

    # Objection Details
    property_description = models.CharField(max_length=255, null=True, blank=True)
    property_physical_address = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    extent = models.CharField(max_length=50, null=True, blank=True)
    market_value = models.DecimalField(max_digits=12, decimal_places=2)
    owner = models.CharField(max_length=20, db_index=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Objection by {self.full_name} ({self.id_number})"
 
    class Meta:
        verbose_name = "Township Objection"
        verbose_name_plural = "Township Objections"


class TownshipObjectionAttachment(models.Model):
    township_objection = models.ForeignKey(TownshipObjection, related_name="township_objection_attachments", on_delete=models.CASCADE)
    file = models.FileField(upload_to="objections/townships/objections")


class TownshipAuthRepAttachment(models.Model):
    auth_rep_attachment = models.ForeignKey(TownshipObjection, related_name="auth_rep_attachments", on_delete=models.CASCADE)
    file = models.FileField(upload_to="objections/townships/authrep")



# Farms Objections
class FarmObjection(BaseObjection):
    #l ink to registered property
    farm_property = models.ForeignKey("property_search.FarmProperty", on_delete=models.CASCADE)
    
    objection_number = models.CharField(max_length=50, unique=True, editable=False, null=True, blank=True)

    # auto generate a unique objection number

    def save(self, *args, **kwargs):
        if not self.objection_number:
            self.objection_number = self.generate_objection_number()
        super().save(*args, **kwargs)
    def generate_objection_number(self):
        sg_code = str(self.farm_property.sg_code_21)
        last_10 = sg_code[-10:] if len(sg_code) >= 10 else sg_code
        random_digit = str(random.randint(0, 9))
        return f"ELMGV25-31-{last_10}-{random_digit}"


    # Objection Category
    YES = "yes"
    NO = "no"
    BOOLEAN_CHOICES = [(YES, "Yes"), (NO, "No")]

    incorrect_valuation = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO)
    omitted_property = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO)

    # Administrative Query (checkboxes → BooleanFields)
    incorrect_owner_name = models.BooleanField(default=False)
    incorrect_category_rating = models.BooleanField(default=False)
    incorrect_extent = models.BooleanField(default=False)
    incorrect_physical_address = models.BooleanField(default=False)
    incorrect_postal_address = models.BooleanField(default=False)
    rates_query = models.BooleanField(default=False)

    # Objection Details
    property_description = models.CharField(max_length=255, null=True, blank=True)
    property_physical_address = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    extent = models.CharField(max_length=50, null=True, blank=True)
    market_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    owner = models.CharField(max_length=20, db_index=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Objection by {self.full_name} ({self.id_number})"
 
    class Meta:
        verbose_name = "Farm Objection"
        verbose_name_plural = "Farm Objections"


class FarmsObjectionAttachment(models.Model):
    farms_objection = models.ForeignKey(FarmObjection, related_name="farms_obection_attachments", on_delete=models.CASCADE)
    file = models.FileField(upload_to="objections/farms/objections")


class FarmsAuthRepAttachment(models.Model):
    auth_rep_attachment = models.ForeignKey(FarmObjection, related_name="auth_rep_attachments", on_delete=models.CASCADE)
    file = models.FileField(upload_to="objections/farms/authrep")
