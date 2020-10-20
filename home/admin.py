from django.contrib import admin
from .models import Slide
from .models import  Page



class SlideAdmin(admin.ModelAdmin):
    list_display= ( 'image_preview', 'title', 'date_posted', 'is_published')
    list_filter =( 'title',)
    prepopulated_fields = {"slug": ('title',)}
    list_editable = ('is_published',)
    list_per_page = 25

    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

admin.site.register(Slide, SlideAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display= ( 'thumbnail_preview', 'title', 'date_posted',  'is_footer_2', 'is_footer_3', 'is_published')
    list_display_links = ('thumbnail_preview', 'title',)
    list_filter =( 'title',)
    prepopulated_fields = {"slug": ('title',)}
    list_editable = ('is_footer_2', 'is_footer_3', 'is_published',)
    list_per_page = 25

    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(Page, PageAdmin)
