from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image
from grades.models import Grade
from accounts.models import CustomUser
#from colors.models import *




# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=100)
    #slug = models.SlugField(max_length=250, blank=False, null=True, unique_for_date='date_posted', help_text="repeat the title here replace spaces with dashes e.g. class alert = class-alert")
    notice = RichTextField(blank=False, null=True)
    author =  models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="notice_author", blank=False, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_grade1 = models.BooleanField(default=False)
    is_grade2 = models.BooleanField(default=False)
    is_grade3 = models.BooleanField(default=False)
    is_grade4 = models.BooleanField(default=False)
    is_grade5 = models.BooleanField(default=False)
    is_grade6 = models.BooleanField(default=False)
    is_grade7 = models.BooleanField(default=False)
    is_grade8 = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    
    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title