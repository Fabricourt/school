from django.contrib import admin
from .models import *


class SubjectAdmin(admin.ModelAdmin):
  list_display = ('subject_name', 'teacher', 'created_by', 'is_published', )
  list_display_links = ('subject_name', 'teacher',)
  list_filter = ('subject_name', 'created_by',)  
  list_editable = ('is_published',)
  search_fields = ('subject_name', 'created_by',  )
  #prepopulated_fields = {"slug": ('subject_name',)}
  list_per_page = 25

admin.site.register(Subject, SubjectAdmin)



class LessonAdmin(admin.ModelAdmin):
  list_display = ('image_preview', 'subject', 'lesson_title','grade_name', )
  list_display_links = ('image_preview', 'lesson_title', )
  list_filter = ('subject', 'lesson_title', 'grade_name', )
  search_fields = ('subject',  'lesson_title', 'grade_name',)
  #prepopulated_fields = {"slug": ('lesson_title',)}
  list_per_page = 25

readonly_fields = ('image_preview',)

def image_preview(self, obj):
    return obj.image_preview

image_preview.short_description = 'Image Preview'
image_preview.allow_tags = True

admin.site.register(Lesson, LessonAdmin)

 
  

class TopicAdmin(admin.ModelAdmin):
  list_display = ('title', 'subject',  )
  list_display_links = ('title',)
  list_filter = ('subject', 'title', )
  search_fields = ('subject',  'title',)
  #prepopulated_fields = {"slug": ('title',)}
  list_per_page = 25

admin.site.register(Topic, TopicAdmin)


class TodayAdmin(admin.ModelAdmin):
  list_display = ('lesson', 'created_by', 'is_published', 'date_posted' )
  list_display_links = ('lesson',)
  list_editable = ('created_by', 'is_published', 'date_posted')
  list_filter = ('lesson', 'created_by', 'is_published', 'date_posted'  )
  search_fields = ('lesson', )
  list_per_page = 25

admin.site.register(Today, TodayAdmin)




class AnswerInline(admin.StackedInline):
  model = Answer
  
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
  list_display = ('title', 'classname', 'subject', 'topic', 'teacher', 'is_published' )
  list_display_links = ('title',)
  list_filter = ('classname', 'subject', 'topic',  'teacher',)
  list_editable = ('is_published', )
  search_fields = ('classname', 'subject', 'topic', 'lesson', 'teacher', 'title',)
  #prepopulated_fields = {"slug": ('title',)}
  list_per_page = 25
  inlines = [AnswerInline]







