from django.contrib import admin
from .models import *



class ServiceAdmin(admin.ModelAdmin):
    list_display= ('title1', 'date_posted', 'is_published')
    list_display_links =( 'title1', )
    list_filter =( 'title1',)
    list_editable = ('is_published',)
    list_per_page = 25

admin.site.register(Service, ServiceAdmin)
