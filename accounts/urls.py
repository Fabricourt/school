from django.urls import path
from . import views
from .views import (
    CustomUserListView,
    CustomUserDetailView,
    CustomUserCreateView,
    CustomUserUpdateView,
    CustomUserDeleteView
)

urlpatterns = [
    path('customusers', CustomUserListView.as_view(), name='customuser-list'),
    path('customuser/<int:pk>/', CustomUserDetailView.as_view(), name='customuser-detail'),
    path('customuser/new/', CustomUserCreateView.as_view(), name='customuser-create'),
    path('customuser/<int:pk>/update/', CustomUserUpdateView.as_view(), name='customuser-update'),
    path('customuser/<int:pk>/delete/', CustomUserDeleteView.as_view(), name='customuser-delete'),

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('welcome', views.welcome, name='welcome'),

    
]