from django.urls import path
from .views import AboutDetailView
from . import views

urlpatterns = [
    path('about/<slug:slug>/', AboutDetailView.as_view(), name='about-detail'),
]
