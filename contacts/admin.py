from django.contrib import admin
from .models import *

admin.site.register(Address)
admin.site.register(Contact_heading)


class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'contact_date',)
  list_display_links = ('name',)
  search_fields = ('name', 'email',)
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)


class ContactusAdmin(admin.ModelAdmin):
  list_display = ('myname', 'teacher', 'heading', 'contact_date',)
  list_display_links = ('myname', 'teacher',)
  search_fields = ('myname', 'teacher', )
  list_filter = ('myname', 'teacher', ) 
  list_per_page = 25

admin.site.register(Contactus, ContactusAdmin)

admin.site.register(Comment)

class TestmonialAdmin(admin.ModelAdmin):
  list_display = ( 'parent_name',  'contact_date', 'is_published')
  list_display_links = ('parent_name',)
  list_editable = ('is_published',)
  search_fields = ('parent_name', )
  list_per_page = 25


admin.site.register(Testmonial, TestmonialAdmin)