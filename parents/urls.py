from django.urls import path
from . import views
from .views import (
    ParentListView,
    UserParentListView,
    ParentDetailView,
    ParentCreateView,
    ParentUpdateView,
    ParentDeleteView
)

urlpatterns = [
    path('parents', ParentListView.as_view(), name='parent-list'),
    path('parent/<int:pk>/', ParentDetailView.as_view(), name='parent-detail'),
    path('parent/new/', ParentCreateView.as_view(), name='parent-create'),
    path('parent/<int:pk>/update/', ParentUpdateView.as_view(), name='parent-update'),
    path('parent/<int:pk>/delete/', ParentDeleteView.as_view(), name='parent-delete'),
    path('user/<str:username>', UserParentListView.as_view(), name='user-parents'),
]
