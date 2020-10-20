from django.contrib import admin
from .models import *


class AboutAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'date_posted', 'is_published')
    list_display_links =( 'image_preview', 'title', )
    list_filter =( 'title',)
    list_editable = ('is_published',)
    list_per_page = 25

    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True
admin.site.register(About, AboutAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'name', 'title', 'date_posted', 'is_mvp',  'is_published')
    list_display_links =( 'image_preview', 'name', 'title', )
    list_filter =( 'name', 'title',)
    prepopulated_fields = {"slug": ('name',)}
    list_editable = ('is_mvp',  'is_published',)
    list_per_page = 25

    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True
admin.site.register(Team, TeamAdmin)