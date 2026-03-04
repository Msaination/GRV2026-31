from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('public', 'Public'),
        ('registered', 'Registered'),
        ('admin', 'Admin'),
    ]

    # Unique identifier across all models
    #min_length=13, max_length=13 to ensure it is a valid ID number format (e.g., South African ID number)
    id_number = models.CharField(max_length=13, unique=True, db_index=True, null=True, blank=True, 
                                verbose_name='South African ID Number',
                                help_text='Enter a valid South African ID number (13 digits).',
                                validators=[
                                    MinLengthValidator(13, message='ID number must be exactly 13 digits.'),
                                    MaxLengthValidator(13, message='ID number must be exactly 13 digits.'),
                                    RegexValidator(r'^\d{13}$', message='ID number must consist of 13 digits only.')
                                ])
    # email = models.EmailField(unique=True, db_index=True) # enforce unique email

    # Role-based access
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='registered', db_index=True)

    # Extra profile fields
    phone_number = models.CharField(max_length=10, null=True, blank=True, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    # Track profile updates
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['id_number']),
            models.Index(fields=['role']),
        ]

    def __str__(self):
        return f"{self.username} ({self.role})"