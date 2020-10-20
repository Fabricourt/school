from django.contrib import admin
from .models import *

class GradeAdmin(admin.ModelAdmin):
  list_display = ('grade_name', 'classteacher', 'classprefect', 'classmonitor',  'is_published', )
  list_display_links = ('grade_name',)
  list_filter = ('grade_name',)
  list_editable = ('is_published',)
  search_fields = ('grade_name', 'classteacher', 'classmonitor', 'classprefect', )
  prepopulated_fields = {"slug": ('grade_name',)}
  list_per_page = 25
  

admin.site.register(Grade, GradeAdmin)
