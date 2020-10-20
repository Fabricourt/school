from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):
  list_display = ( 'student_name', 'parent_father', 'parent_mother', 'parent_guardian', 'is_mvp', 'is_published', 'account_date')
  list_display_links = ('student_name',)
  list_filter = ('parent_father', 'parent_mother', 'parent_guardian')
  search_fields = ('student_name', 'parent_father', 'parent_mother', 'parent_guardian')
  list_editable = ('is_mvp', 'is_published')
  list_per_page = 25

admin.site.register(Student, StudentAdmin)