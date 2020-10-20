from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
            'image_preview',
            'username',
            'title',
            'first_name',
            'last_name',
            'phone', 
            'email', 

          
        
            
            ]
    list_display_links = ('image_preview', 'username',)
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = (
            'is_teacher',
            'is_student',
            'is_parent',
            'is_admin',
            'is_headmaster',
            'is_deputy_headmaster',
            'is_senior_teacher',
            'is_grade1',
            'is_grade2',
            'is_grade3',
            'is_grade4',
            'is_grade5',
            'is_grade6',
            'is_grade7',
            'is_grade8',
           

    )  
  
    fieldsets = (
            *UserAdmin.fieldsets,  # original form fieldsets, expanded
            (                      # new fieldset added on to the bottom
                'Choose User Roles',  # group heading of your choice; set to None for a blank space instead of a header
                {
                    'fields': (
                        'title',
                        'home',
                        'address',
                        'phone',
                        'is_teacher',
                        'is_student',
                        'is_parent',
                        'is_admin',
                        'is_headmaster',
                        'is_deputy_headmaster',
                        'is_senior_teacher', 
                        'is_grade1',
                        'is_grade2',
                        'is_grade3',
                        'is_grade4',
                        'is_grade5',
                        'is_grade6',
                        'is_grade7',
                        'is_grade8',
                        'image',

                    ),
                    
                },
                
            ),
            
        )    
readonly_fields = ('image_preview',)

def image_preview(self, obj):
    return obj.image_preview

image_preview.short_description = 'Image Preview'
image_preview.allow_tags = True

admin.site.register(CustomUser, CustomUserAdmin)
