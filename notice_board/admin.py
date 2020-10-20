from django.contrib import admin
from .models import *

class NoticeAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'created_by', 'date_posted', 'is_published', )
  list_display_links = ('title', 'author')
  list_filter = ('title',)
  list_editable = ('is_published',)
  search_fields = ('title', 'author', )
  prepopulated_fields = {"slug": ('title',)}
  list_per_page = 25
  

admin.site.register(Notice, NoticeAdmin)
