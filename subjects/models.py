from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import CustomUser
#from colors.models import *
from ckeditor.fields import RichTextField
from grades.models import *
from django.utils.html import mark_safe
from PIL import Image
from teachers.models import Teacher



# Subject
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=250,unique_for_date='date_posted')
    specific_grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='eg class 7')
    teacher = models.ForeignKey(CustomUser, related_name='subject_teacher', on_delete=models.DO_NOTHING, blank=False, null=True)
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

    class Meta:
        verbose_name = 'Learning_area'
        verbose_name_plural = 'Learning_areas'
        ordering = ['subject_name']
    

    def get_absolute_url(self):
        return reverse('subject-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.subject_name

    
#Topic
class Topic(models.Model):
    subject = models.ForeignKey(Subject,  on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(max_length=200, blank=False, null= True)
    slug = models.SlugField(max_length=200, blank=False, null=True, unique=True)
    grade_name = models.ForeignKey(Grade, on_delete=models.CASCADE)
    overview = RichTextField(blank=True, null=True, help_text='input specific learning outcomes, val-ues, pcl, & core competence')
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_grade1 = models.BooleanField(default=False)
    is_grade2 = models.BooleanField(default=False)
    is_grade3 = models.BooleanField(default=False)
    is_grade4 = models.BooleanField(default=False)
    is_grade5 = models.BooleanField(default=False)
    is_grade6 = models.BooleanField(default=False)
    is_grade7 = models.BooleanField(default=False)
    is_grade8 = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Strand'
        verbose_name_plural = 'Strands'
        ordering = ['date_posted']

    def get_absolute_url(self):
        return reverse('topic-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

#Lesson
class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='lesson_teacher', on_delete=models.DO_NOTHING, blank=False, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,  on_delete=models.CASCADE, blank=False, null=True)
    lesson_title = models.CharField(max_length=100, blank=False, null=True)
    slug = models.SlugField(max_length=250, blank=False, null=True, unique_for_date='date_posted')
    grade_name = models.ForeignKey(Grade, on_delete=models.CASCADE)
    videofile= models.FileField(upload_to='lesson_videos/%Y/%m/%d', null=True, blank=True)
    content = models.TextField(blank=False, null=True)
    lesson_pic1 = models.ImageField(upload_to='lesson_pics/%Y/%m/%d/',null=True, blank=True)
    lesson_pic2 = models.ImageField(upload_to='lesson_pics/%Y/%m/%d/',null=True, blank=True)
    lesson_pic3 = models.ImageField(upload_to='lesson_pics/%Y/%m/%d/',null=True, blank=True)
    lesson_pic4 = models.ImageField(upload_to='lesson_pics/%Y/%m/%d/',null=True, blank=True)
    lesson_pic5 = models.ImageField(upload_to='lesson_pics/%Y/%m/%d/',null=True, blank=True)
    lesson_pic6 = models.ImageField(upload_to='lesson_pics/%Y/%m/%d/',null=True, blank=True)
    lesson_pic7 = models.ImageField(upload_to='lesson_pics/%Y/%m/%d/',null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,  blank=False, null=True)
    is_mvp = models.BooleanField(default=False, help_text="click this if this is pp1, pp2, grade_1, grade_2, grade_3")
    is_grade1 = models.BooleanField(default=False)
    is_grade2 = models.BooleanField(default=False)
    is_grade3 = models.BooleanField(default=False)
    is_grade4 = models.BooleanField(default=False)
    is_grade5 = models.BooleanField(default=False)
    is_grade6 = models.BooleanField(default=False)
    is_grade7 = models.BooleanField(default=False)
    is_grade8 = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    @property
    def image_preview(self):
        if self.lesson_pic1:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.lesson_pic1.url))
        return "" 
    

    class Meta:
        verbose_name = 'Sub_strand'
        verbose_name_plural = 'Sub_strands'

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.lesson_title

STATUS = ((0, "Draft"), (1, "Publish"))



#Exercise
class Exercise(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True, unique=True)
    slug = models.SlugField(max_length=200, blank=False, null=True, unique=True)
    questions = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, null=True,)
    questions_typed = RichTextField(blank=True, null=True)
    exercise_answers = RichTextField(blank=True, null=True)
    answers_explanation = models.FileField(upload_to='exercise_videos/%Y/%m/%d', null=True, blank=True)
    classname = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=False, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING,  blank=False, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING,  blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING,  blank=True, null=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="teacher_questions")
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    is_grade1 = models.BooleanField(default=False)
    is_grade2 = models.BooleanField(default=False)
    is_grade3 = models.BooleanField(default=False)
    is_grade4 = models.BooleanField(default=False)
    is_grade5 = models.BooleanField(default=False)
    is_grade6 = models.BooleanField(default=False)
    is_grade7 = models.BooleanField(default=False)
    is_grade8 = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)


    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("exercise", kwargs={"slug": str(self.slug)})



class Answer(models.Model):
    name = models.ForeignKey(CustomUser,  on_delete=models.CASCADE, blank=True, null=True, related_name="studentAnswering")
    #upload = models.FileField(upload_to='files/%Y/%m/%d/', default='blank.pdf', blank=True, null=True, help_text="upload your answer doc here")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="answers")
    answers_typed = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    unmarked = models.BooleanField(default=True, null=True, blank=True, help_text="do not click on this unless advised otherwise")

    

    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return "Answer {} by {}".format(self.exercise, self.name)


    def get_absolute_url(self):
        return reverse('answer-detail', kwargs={'pk': self.pk})

class Today(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='today_teacher', on_delete=models.DO_NOTHING, blank=False, null=True)
    lesson = models.ForeignKey(Lesson,  on_delete=models.CASCADE, blank=False, null=True)
    exercise = models.ForeignKey(Exercise,  on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=False, null=True)
    is_grade1 = models.BooleanField(default=False)
    is_grade2 = models.BooleanField(default=False)
    is_grade3 = models.BooleanField(default=False)
    is_grade4 = models.BooleanField(default=False)
    is_grade5 = models.BooleanField(default=False)
    is_grade6 = models.BooleanField(default=False)
    is_grade7 = models.BooleanField(default=False)
    is_grade8 = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.lesson.lesson_title