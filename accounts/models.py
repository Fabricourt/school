from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import mark_safe
from django.urls import reverse
from PIL import Image


class CustomUser(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='account_pics')
    phone = models.CharField(max_length=200, blank=True, null=True)
    home = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_prefect = models.BooleanField(default=False)
    is_monitor = models.BooleanField(default=False)
    is_headboy = models.BooleanField(default=False)
    is_headgirl = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_headmaster = models.BooleanField(default=False)
    is_deputy_headmaster = models.BooleanField(default=False)
    is_senior_teacher = models.BooleanField(default=False)
    is_grade1 = models.BooleanField(default=False)
    is_grade2 = models.BooleanField(default=False)
    is_grade3 = models.BooleanField(default=False)
    is_grade4 = models.BooleanField(default=False)
    is_grade5 = models.BooleanField(default=False)
    is_grade6 = models.BooleanField(default=False)
    is_grade7 = models.BooleanField(default=False)
    is_grade8 = models.BooleanField(default=False)
   
  
    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return "" 

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('customuser-detail', kwargs={'pk': self.pk})

    def save(self, **kwargs):
        super().save()
 
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)