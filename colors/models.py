from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from PIL import Image

# Create your models here.


class Color(models.Model):
    text_color = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    border_color = models.CharField(max_length=100)
    bg_color = models.CharField(max_length=100)
    hover_border_color = models.CharField(max_length=100)
    hover_color = models.CharField(max_length=100)
    hover_text_color = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='color_pics')

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100%" height="50" />'.format(self.image.url))
        return "" 

    def __str__(self):
        return self.color

    def save(self, **kwargs):
        super().save()
 
        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)


