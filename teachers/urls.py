from django.urls import path

from . import views

urlpatterns = [
    path('teachers', views.teachers, name='teachers'),
    path('<int:teacher_id>', views.teacher, name='teacher'),
   
]