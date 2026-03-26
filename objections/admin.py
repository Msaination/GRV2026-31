from django.contrib import admin
from .models import TownshipObjection, FarmObjection, TownshipAuthRepAttachment, TownshipObjectionAttachment, FarmsObjectionAttachment, FarmsAuthRepAttachment


class TownshipObjectionAttachmentInline(admin.TabularInline):
    model = TownshipObjectionAttachment
    extra = 1   # show one empty slot by default
    fields = ("file",)  # only show the file field


class TownshipAuthRepAttachmentInline(admin.TabularInline):
    model = TownshipAuthRepAttachment
    extra = 1
    fields = ("file",)


class FarmsObjectionAttachmentInline(admin.TabularInline):
    model = FarmsObjectionAttachment
    extra = 1   # show one empty slot by default
    fields = ("file",)  # only show the file field


class FarmsAuthRepAttachmentInline(admin.TabularInline):
    model = FarmsAuthRepAttachment
    extra = 1   # show one empty slot by default
    fields = ("file",)  # only show the file field



@admin.register(TownshipObjection)
class TownshipObjection(admin.ModelAdmin):
    list_display = (
        'objection_number',
        'objector_status',
        'not_owner_description',
        'township_objection_attachments',
        'auth_rep_attachments'
    )

    inlines = [TownshipObjectionAttachmentInline, TownshipAuthRepAttachmentInline]

    list_filter = ('objector_status', 'not_owner_description')
    search_fields = ('objector_status', 'not_owner_description')

    def township_objection_attachments(self, obj):
        return obj.township_objection_attachments.count()
    township_objection_attachments.short_description = "Objection Attachments"

    def auth_rep_attachments(self, obj):
        return obj.auth_rep_attachments.count()
    auth_rep_attachments.short_description = "Auth Attachments"


@admin.register(FarmObjection)
class FarmObjection(admin.ModelAdmin):
    list_display = ('objection_number', 
                    'objector_status',
                    'not_owner_description',
                    'farms_obection_attachments',
                    'auth_rep_attachments'
                    )
    list_filter = ('objector_status', 'not_owner_description')
    search_fields = ('objector_status', 'not_owner_description')

    inlines = [FarmsObjectionAttachmentInline, FarmsAuthRepAttachmentInline]

    def farms_obection_attachments(self, obj):
        return obj.farms_obection_attachments.count()
    farms_obection_attachments.short_description = "Objection Attachments"

    def auth_rep_attachments(self, obj):
        return obj.auth_rep_attachments.count()
    auth_rep_attachments.short_description = "Auth Attachments"