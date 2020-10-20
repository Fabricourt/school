from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('central', views.central, name='central'),

]

