from . import views
from django.urls import path, include
from .views import (

    NoticeListView,
    NoticeDetailView,
    NoticeUpdateView,
    NoticeDeleteView,
    NoticeCreateView,
    UserNoticeListView,
   

)


urlpatterns = [
    path('notices', NoticeListView.as_view(), name='notice-list'),
    path('notice/<int:pk>/', NoticeDetailView.as_view(), name='notice-detail'),
    path('notice/new/', NoticeCreateView.as_view(), name='notice-create'),
    path('notice/<int:pk>/update/', NoticeUpdateView.as_view(), name='notice-update'),
    path('notice/<int:pk>/delete/', NoticeDeleteView.as_view(), name='notice-delete'),
    path('user/<str:username>', UserNoticeListView.as_view(), name='user-notices'),
   
]   