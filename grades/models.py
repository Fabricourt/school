from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import CustomUser
from ckeditor.fields import RichTextField
from PIL import Image
from colors.models import Color


#from lessons.models import *





class Grade(models.Model):
    grade_name = models.CharField(max_length=100, blank=False, null=True)
    slug = models.SlugField(max_length=250, blank=False, null=True, unique_for_date='date_posted', help_text='You must re enter the class name using dashes e.g class 7 west = class-7-west on the slug field')
    classteacher =  models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="class_teacher", blank=False, null=True)
    classmonitor = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="class_monitor",blank=False, null=True)
    classprefect = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="class_prefect",blank=False, null=True)
    colors = models.ForeignKey(Color, on_delete=models.DO_NOTHING, blank=False, null=True)
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
    is_mvp = models.BooleanField(default=False, help_text="click this if this is pp1, pp2, grade_1, grade_2, grade_3")


    def get_absolute_url(self):
        return reverse('grade-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.grade_name
