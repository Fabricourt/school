from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image
from django.utils.html import mark_safe
from django.utils.html import format_html


class Slide(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=False, null=True, unique=True)
    label = models.CharField(max_length=200)
    #description = models.TextField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=False)

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return "" 
   

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        super().save()
 

        img = Image.open(self.image.path)

        if img.height > 1680 or img.width > 800:
            output_size = (1680, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('slide-detail', kwargs={'slug': self.slug})




class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=False, null=True, unique=True)
    statement = models.CharField(max_length=400)
    thumbnail = models.ImageField(upload_to='Pages/%Y/%m/%d/', null=True, blank=False)
    description = RichTextField()      
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    #is_footer_1 = models.BooleanField(default=False)
    is_footer_2 = models.BooleanField(default=False)
    is_footer_3 = models.BooleanField(default=False)
  
    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.thumbnail.url))
        return ""    

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'slug': self.slug})