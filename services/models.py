from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from PIL import Image



class Service(models.Model):
    title1 = models.CharField(max_length=200, blank=False, null=True)
    title2 = models.CharField(max_length=200, blank=False, null=True)
    title3 = models.CharField(max_length=200, blank=False, null=True)
    title4 = models.CharField(max_length=200, blank=False, null=True)
    subtitle1 = models.CharField(max_length=200, blank=False, null=True)
    subtitle2 = models.CharField(max_length=200, blank=False, null=True)
    subtitle3 = models.CharField(max_length=200, blank=False, null=True)
    subtitle4 = models.CharField(max_length=200, blank=False, null=True)
    statement1 = models.CharField(max_length=50, blank=False, null=True)
    statement2 = models.CharField(max_length=50, blank=False, null=True)
    statement3 = models.CharField(max_length=50, blank=False, null=True)
    statement4 = models.CharField(max_length=50, blank=False, null=True)
    icon1 = models.CharField(max_length=200, blank=False, null=True)
    icon2 = models.CharField(max_length=200, blank=False, null=True)
    icon3 = models.CharField(max_length=200, blank=False, null=True)
    icon4 = models.CharField(max_length=200, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    #image = models.ImageField(upload_to='Service/%Y/%m/%d/', null=True, blank=False)

    def __str__(self):
        return str(self.title1)



    