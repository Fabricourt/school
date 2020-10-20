from django.urls import path
from . import views
from .views import (
    #ClassListView,
    #ClassDetailView,
    #Class_nameListView,
    ParentDetailView,
    #ClassCreateView,
    #ClassUpdateView,
    #ClassDeleteView
)

urlpatterns = [
    path('parent/<int:pk>/', ParentDetailView.as_view(), name='parent-detail'),
]
