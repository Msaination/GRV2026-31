from django.db import models
# from users.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

def validate_sg_code_21(value): 
    if len(value) != 21: 
        raise ValidationError("SG Code 21 must be exactly 21 characters long.")

class BaseProperty(models.Model):
    # id_number = models.CharField(max_length=20)  # links to User.id_number
    id_number = models.CharField(max_length=13, db_index=True, null=True, blank=True, 
                                verbose_name='South African ID Number',
                                help_text='Enter a valid South African ID number (13 digits).',
                                validators=[
                                    MinLengthValidator(13, message='ID number must be exactly 13 digits.'),
                                    RegexValidator(r'^\d{13}$', message='ID number must consist of 13 digits only.')
                                ]) 


    class Meta:
        abstract = True


    #FarmProperty inherits from BaseProperty and adds specific fields for farm properties

class FarmProperty(BaseProperty):
    sg_code_21 = models.CharField(max_length=21, db_index=True, validators=[validate_sg_code_21])
    min_code = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    grv = models.CharField(max_length=50, db_index=True)
    regdiv = models.CharField(max_length=50, db_index=True)
    farm_name = models.CharField(max_length=100, db_index=True)
    sectional_title = models.CharField(max_length=100, null=True, blank=True)
    erf_no = models.CharField(max_length=50, db_index=True)
    ptn = models.CharField(max_length=10, db_index=True)  
    unit = models.CharField(max_length=10, db_index=True)  
    extent = models.CharField(max_length=50)
    ha = models.CharField(max_length=50)
    physical_address = models.CharField(max_length=255, db_index=True)
    owner = models.CharField(max_length=20, db_index=True)
    market_value = models.DecimalField(max_digits=12, decimal_places=2)
    owner_status = models.CharField(max_length=20, db_index=True)
    category = models.CharField(max_length=30, db_index=True)
    remarks = models.TextField(null=True, blank=True)
    related_name="farm_properties",# 👈 allows reverse lookup

    def __str__(self):
        return self.farm_name
    

class Meta:
    indexes = [
        models.Index(fields=['sg_code_21']),
        models.Index(fields=['registered_owner']),
    ]
    verbose_name = "Farm Property"
    verbose_name_plural = "Farm Properties"



