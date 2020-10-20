from django.urls import path
from . import views
from django.urls import path, include
from .views import (
    #UserContactustListView,
    ContactusDetailView,
    #ContactusUpdateView,
    #UserExerciseListView,
    ContactusCreateView,
    TestmonialCreateView,
    #ContactusDeleteView,
    
)


urlpatterns = [
    path('contacts', views.contact, name='contact'),
    path('testmonial/new/', TestmonialCreateView.as_view(), name='testmonial-create'),
    path('contactus/new/', ContactusCreateView.as_view(), name='contactus-create'),
    path('contactus/<int:pk>/', ContactusDetailView.as_view(), name='contactus-detail'),
    #path('contactus/<int:pk>/update/', ContactusUpdateView.as_view(), name='Contactus-update'),
    #path('contactus/<int:pk>/delete/', ContactusDeleteView.as_view(), name='Contactus-delete'),
    #path('<int:Contactus_id>', views.Contactus, name='Contactus'),
]   