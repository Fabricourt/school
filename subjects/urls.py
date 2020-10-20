from . import views
from django.urls import path, include
from .views import (
    #UserAnswertListView,
    AnswerDetailView,
    AnswerUpdateView,
    UserExerciseListView,
    AnswerCreateView,
    AnswerDeleteView,
    LessonDetailView,
    ExerciseDetail,
)


urlpatterns = [

    path('lesson/<slug:slug>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('exercise-list', views.ExerciseList.as_view(), name='exercise-list'),
    path('exercise/<slug:slug>/', ExerciseDetail.as_view(), name='exercise-detail'),
    path("<slug:slug>/", views.exercise, name="exercise-"),
    path('answer/new/', AnswerCreateView.as_view(), name='answer-create'),
    path('answer/<int:pk>/', AnswerDetailView.as_view(), name='answer-detail'),
    path('answer/<int:pk>/update/', AnswerUpdateView.as_view(), name='answer-update'),
    path('answer/<int:pk>/delete/', AnswerDeleteView.as_view(), name='answer-delete'),
    path('<int:answer_id>', views.answer, name='answer'),
    path('user/<str:username>', UserExerciseListView.as_view(), name='user-exercises'),
]   