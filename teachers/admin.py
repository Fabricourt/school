from django.contrib import admin

from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
  list_display = ( 'name', 'hire_date')
  list_display_links = ( 'name',)
  search_fields = ('name',)
  list_per_page = 25

admin.site.register(Teacher, TeacherAdmin)