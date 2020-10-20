from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from accounts.models import CustomUser

class Teacher(models.Model):
    name =  models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="teacher_name", blank=False, null=True)
    description = models.TextField(blank=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
      return self.name.first_name

    def get_absolute_url(self):
        return reverse('teacher', kwargs={'pk': self.pk})

 