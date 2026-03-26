from django.contrib import admin
from .models import TownshipProperty

@admin.register(TownshipProperty)
class TownshipProperty(admin.ModelAdmin):
    list_display = ('sg_code_21', 'prop_class', 'township')
    search_fields = ('registered_owner','sg_code_21', 'prop_class', 'township')
    list_filter = ('category', 'owner_status')