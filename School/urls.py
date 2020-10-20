from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('teachers/', include('teachers.urls')),
    path('subjects/', include('subjects.urls')),
    path('parents/', include('parents.urls')),
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
    path('accounts/', include('accounts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

