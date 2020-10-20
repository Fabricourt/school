from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.utils.html import mark_safe
from PIL import Image

        
class Photo(models.Model):
  title  = models.CharField(max_length=120, blank=False, null=True)
  description = RichTextField(blank=True, null=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  title_1 = models.CharField(max_length=200, null=True, blank=False)
  statement_1 = models.CharField(max_length=200, null=True, blank=False)
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  title_2 = models.CharField(max_length=200, null=True, blank=False)
  statement_2 = models.CharField(max_length=200, null=True, blank=False)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  title_3 = models.CharField(max_length=200, null=True, blank=False)
  statement_3 = models.CharField(max_length=200, null=True, blank=False)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  title_4 = models.CharField(max_length=200, null=True, blank=False)
  statement_4 = models.CharField(max_length=200, null=True, blank=False)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  title_5 = models.CharField(max_length=200, null=True, blank=False)
  statement_5 = models.CharField(max_length=200, null=True, blank=False)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  title_6 = models.CharField(max_length=200, null=True, blank=False)
  statement_6 = models.CharField(max_length=200, null=True, blank=False)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  title_7 = models.CharField(max_length=200, null=True, blank=False)
  statement_7 = models.CharField(max_length=200, null=True, blank=False)
  photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  title_8 = models.CharField(max_length=200, null=True, blank=False)
  statement_8 = models.CharField(max_length=200, null=True, blank=False)
  photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  title_9 = models.CharField(max_length=200, null=True, blank=False)
  statement_9 = models.CharField(max_length=200, null=True, blank=False)
  photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  is_published = models.BooleanField(default=True)
  date_posted = models.DateTimeField(default=timezone.now)
  created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=False, null=True)

  @property
  def image_preview(self):
    if self.photo_main:
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.photo_main.url))
    return "" 

  def __str__(self):
    return self.title