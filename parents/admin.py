from django.contrib import admin

from .models import Parent

class ParentAdmin(admin.ModelAdmin):
  list_display = ( 'name', 'account_date')
  list_display_links = ( 'name',)
  search_fields = ('name',)
  list_per_page = 25

admin.site.register(Parent, ParentAdmin)