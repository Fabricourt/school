from django.urls import path
from . import views
from .views import (
    TeacherListView,
    UserTeacherListView,
    TeacherDetailView,
    TeacherCreateView,
    TeacherUpdateView,
    TeacherDeleteView
)

urlpatterns = [
    path('teachers', TeacherListView.as_view(), name='teacher-list'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('teacher/new/', TeacherCreateView.as_view(), name='teacher-create'),
    path('teacher/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher-update'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),
    path('user/<str:username>', UserTeacherListView.as_view(), name='user-teachers'),
    path('teachers', views.teachers, name='teachers'),
    path('<int:teacher_id>', views.teacher, name='teacher'),
   
]