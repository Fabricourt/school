from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from PIL import Image

 
class About(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='about', blank=False, null=True, unique=True)
    statement = models.CharField(max_length=400)
    #description = RichTextField()
    welcome_message = RichTextField(max_length=600, null=True, blank=False)
    aboutourleaders = RichTextField(max_length=500, blank=False, null=True)
    title1 = models.CharField(max_length=200, null=True, blank=False)
    icon1 = models.CharField(max_length=200, null=True, blank=False)
    about_us_1 = models.CharField(max_length=200, null=True, blank=False)
    aboutusimage1 = models.ImageField(upload_to='About/%Y/%m/%d/', null=True, blank=False)
    title2 = models.CharField(max_length=200, null=True, blank=False)
    icon2 = models.CharField(max_length=200, null=True, blank=False)
    about_us_2 = models.CharField(max_length=200, null=True, blank=False)
    aboutusimage2 = models.ImageField(upload_to='About/%Y/%m/%d/', null=True, blank=False)
    title3 = models.CharField(max_length=200, null=True, blank=False)
    icon3 = models.CharField(max_length=200, null=True, blank=False)
    about_us_3 = models.CharField(max_length=200, null=True, blank=False)
    aboutusimage3 = models.ImageField(upload_to='About/%Y/%m/%d/', null=True, blank=False)
    title4 = models.CharField(max_length=200, null=True, blank=False)
    number4 = models.CharField(max_length=200, null=True, blank=False)
    about_us_4 = models.CharField(max_length=200, null=True, blank=False)
    aboutusimage4 = models.ImageField(upload_to='About/%Y/%m/%d/', null=True, blank=False)
    title5 = models.CharField(max_length=200, null=True, blank=False)
    number5 = models.CharField(max_length=200, null=True, blank=False)
    about_us_5 = models.CharField(max_length=200, null=True, blank=False)
    aboutusimage5 = models.ImageField(upload_to='About/%Y/%m/%d/', null=True, blank=False)
    title6 = models.CharField(max_length=200, null=True, blank=False)
    number6 = models.CharField(max_length=200, null=True, blank=False)
    about_us_6 = models.CharField(max_length=200, null=True, blank=False)
    aboutusimage6 = models.ImageField(upload_to='About/%Y/%m/%d/', null=True, blank=False)
    title7 = models.CharField(max_length=200, null=True, blank=False)
    number7 = models.CharField(max_length=200, null=True, blank=False)
    about_us_7 = models.CharField(max_length=200, null=True, blank=False)
    aboutusimage7 = models.ImageField(upload_to='About/%Y/%m/%d/', null=True, blank=False)
    testimonial_parent_image = models.ImageField(upload_to='About/%Y/%m/%d/', null=True, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='About/%Y/%m/%d/', null=True, blank=False)


    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return "" 

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        ordering = ['date_posted']

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('about-detail', kwargs={'slug': self.slug})


class Team(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,  blank=False, null=True, unique=True)
    title = models.CharField(max_length=200)
    statement = models.CharField(max_length=200, blank=False, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_mvp = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='Team/%Y/%m/%d/', null=True, blank=False)

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return "" 

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Triza Academy Team'
        ordering = ['date_posted']


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('team-detail', kwargs={'slug': self.slug})

