from django.contrib import admin
from .models import *

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
  list_display = ('image_preview', 'title', 'is_published' )
  list_display_links = ('image_preview', 'title', )
  list_filter = ('title',  )
  search_fields = ('title',  )
  list_editable = ('is_published',)
  list_per_page = 25

readonly_fields = ('image_preview',)

def image_preview(self, obj):
    return obj.image_preview

image_preview.short_description = 'Image Preview'
image_preview.allow_tags = True

admin.site.register(Photo, PhotoAdmin)