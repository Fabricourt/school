from django.urls import path
from .views import PageDetailView
from . import views

urlpatterns = [
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page-detail'),
]
