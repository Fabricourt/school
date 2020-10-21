from django.contrib import admin
from .models import *

class GradeAdmin(admin.ModelAdmin):
  list_display = ('grade_name', 'class_teacher', 'class_prefect', 'class_monitor',  'is_published', )
  list_display_links = ('grade_name',)
  list_filter = ('grade_name',)
  list_editable = ('is_published',)
  search_fields = ('grade_name', 'class_teacher', 'class_monitor', 'class_prefect', )
  prepopulated_fields = {"slug": ('grade_name',)}
  list_per_page = 25
  

admin.site.register(Grade, GradeAdmin)