# Copyright (C) 2014 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

from django.contrib import admin
from django.contrib.contenttypes import generic

from painlessseo.models import SeoMetadata, register_seo_signals


class SeoMetadataInline(generic.GenericStackedInline):
    model = SeoMetadata
    extra = 0
    max_num = 0
    exclude = ('path', 'lang_code', 'override_path')

    def has_delete_permission(self, request, obj=None):
        return False


class SeoMetadataAdmin(admin.ModelAdmin):
    list_display = ('path', 'lang_code', )
    search_fields = ['path', ]
    list_filter = ('lang_code', )
    exclude = ('content_type', 'object_id', 'override_path')

    def get_readonly_fields(self, request, obj):
        if obj and obj.override_path:
            return ['path', 'lang_code']
        return []

admin.site.register(SeoMetadata, SeoMetadataAdmin)
register_seo_signals()
