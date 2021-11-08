from currency.models import ContactUs, Rate, Source
from currency.resources import RateResource

from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from rangefilter.filters import DateTimeRangeFilter


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'source',
        'created',
    )

    list_filter = (
        'type',
        ('created', DateTimeRangeFilter),
    )

    search_fields = (
        'buy',
        'sale',
        'source',
    )

    readonly_fields = (
        'buy',
        'sale',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'email_from',
        'subject',
        'message',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'source_url',
        'name',
    )


admin.site.register(Rate, RateAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Source, SourceAdmin)
