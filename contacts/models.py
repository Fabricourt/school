from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from teachers.models import Teacher
from parents.models import Parent
from students.models import Student
from django.urls import reverse
from django.utils.html import mark_safe
from PIL import Image

class Address(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    statement = models.CharField(max_length=100, blank=False, null=True)
    logo = models.ImageField(upload_to='logo/%Y/%m/%d/', null=True, blank=False)
    address = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    phone = models.CharField(max_length=100, null= True, blank=False)
    phone_1 = models.CharField(max_length=100, null= True, blank=False)
    instagram = models.CharField(max_length=100, null= True, blank=False)
    facebook = models.CharField(max_length=100, null= True, blank=False)
    twitter = models.CharField(max_length=100, null= True, blank=False)
    youtube = models.CharField(max_length=100, null= True, blank=False)
    worktime = models.CharField(max_length=100, null= True, blank=False, help_text="office time Mon-Fri 09:00-17:00")
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'
        

class Contact_heading(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True,)
    contact_statement = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Heading'
        verbose_name_plural = 'Heading'
        ordering = ['date_posted']

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    message = models.TextField(null=True, blank=False)
    contact_date = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})


class Contactus(models.Model):
    heading = models.CharField(max_length=200, blank=False, null=True)
    message = models.TextField(null=True, blank=False)
    myname = models.ForeignKey(Student,  on_delete=models.CASCADE, blank=False, null=True, related_name="studentname")
    teacher = models.ForeignKey(Teacher,  on_delete=models.CASCADE, blank=False, null=True, related_name="teachertalk")
    contact_date = models.DateTimeField(default=timezone.now, null=True, blank=True)

    class Meta:
        verbose_name = 'contactus'
        verbose_name_plural = 'contactus'
       

    def __str__(self):
        return self.heading


    def get_absolute_url(self):
        return reverse('contactus-detail',  kwargs={'pk': self.pk})

class Comment(models.Model):
    contactus = models.ForeignKey('contacts.Contactus', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Testmonial(models.Model):
    parent_name = models.ForeignKey(Parent,  on_delete=models.CASCADE, blank=False, null=True, related_name="myparent")
    message = models.TextField(null=True, blank=False)
    contact_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    is_published = models.BooleanField(default=False)

    
    def __str__(self):
        return self.parent_name.name.first_name


    def get_absolute_url(self):
        return reverse('feedback-detail',  kwargs={'pk': self.pk})