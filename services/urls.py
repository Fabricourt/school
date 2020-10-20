from django.urls import path
from .views import ServiceDetailView
from .views import SolutionDetailView
from . import views

urlpatterns = [
    path('service/<slug:slug>/', ServiceDetailView.as_view(), name='service-detail'),
    path('solution/<slug:slug>/', SolutionDetailView.as_view(), name='solution-detail'),
]
