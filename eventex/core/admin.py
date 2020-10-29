from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Speaker


class SpeakerModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'website_link']

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

admin.site.register(Speaker, SpeakerModelAdmin)
