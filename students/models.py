from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from accounts.models import CustomUser
from teachers.models import *
from parents.models import *



    

class Student(models.Model):
    student_name =  models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="student_name", blank=False, null=True)
    contact_parent =  models.ForeignKey(Parent, on_delete=models.DO_NOTHING,  blank=True, null=True)
    parent_father =  models.ForeignKey(Parent, on_delete=models.DO_NOTHING, related_name="father", blank=True, null=True)
    parent_mother =  models.ForeignKey(Parent, on_delete=models.DO_NOTHING, related_name="mother", blank=True, null=True)
    parent_guardian =  models.ForeignKey(Parent, on_delete=models.DO_NOTHING, related_name="guardian", blank=True, null=True)
    mathematics_teacher =  models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name="mathematicsteacher", blank=True, null=True)
    social_studies_teacher =  models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name="socialstudiesteacher", blank=True, null=True)
    science_teacher =  models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name="scienceteacher", blank=True, null=True)
    kiswahili_teacher =  models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name="kiswahiliteacher", blank=True, null=True)
    english_teacher =  models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name="englishteacher", blank=True, null=True)
    bio = models.TextField(blank=True)
    is_mvp = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    account_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
      return self.student_name.first_name

    def get_absolute_url(self):
        return reverse('teacher', kwargs={'pk': self.pk})

 