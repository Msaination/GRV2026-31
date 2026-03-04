from django.contrib import admin

# Register your models here.
from .models import FarmProperty
@admin.register(FarmProperty)
class FarmPropertyAdmin(admin.ModelAdmin):
    list_display = ('sg_code_21', 'farm_name', 'physical_address', 'market_value')
    search_fields = ('sg_code_21', 'farm_name', 'physical_address')
    list_filter = ( 'category', 'owner_status')

    # Organize fields in the detail views
    fieldsets = (
        ('Ownership', {'fields': ('id_number', 'sg_code_21', 'owner', 'owner_status')}),
        ('Additional Info', {'fields': ('farm_name', 'min_code', 'grv', 'regdiv', 'sectional_title', 'erf_no', 'ptn', 'unit', 'extent', 'ha', 'category', 'remarks')}),
    )
    

    # Fields shown when creating a new property
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('sg_code_21', 'farm_name', 'physical_address', 'market_value'),
        }),
    )