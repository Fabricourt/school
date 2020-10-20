from django.contrib import admin
from .models import Color


class ColorAdmin(admin.ModelAdmin):
  list_display = ('color', 'image_preview', )
  list_display_links = ('image_preview', 'color',)
  list_filter = ('color',)
  search_fields = ('color',  )
  list_per_page = 25

readonly_fields = ('image_preview',)

def image_preview(self, obj):
    return obj.image_preview

image_preview.short_description = 'Image Preview'
image_preview.allow_tags = True

admin.site.register(Color, ColorAdmin)