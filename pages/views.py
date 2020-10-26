from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from services.models import *
from contacts.models import *
from home.models import Slide, Page
from about.models import About, Team
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from subjects.models import *
from students.models import *
from parents.models import *
from grades.models import *
from notice_board.models import Notice
from colors.models import Color
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from subjects.models import *
from gallerys.models import *
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)





def index(request):
    abouts = About.objects.order_by('date_posted').filter(is_published=True)[:1]
    photos = Photo.objects.order_by('date_posted').filter(is_published=True)[:8]
    slides = Slide.objects.order_by('date_posted').filter(is_published=True)
    teams = Team.objects.order_by('date_posted').filter(is_published=True)
    services = Service.objects.order_by('date_posted').filter(is_published=True)[:8]
    heading = Contact_heading.objects.order_by('date_posted').filter(is_published=True)[:1]
    addresss = Address.objects.all()
    testmonials = Testmonial.objects.order_by('-contact_date').filter(is_published=True)[:3]
    #f1_pages = Page.objects.all().filter(is_footer_1=True)[:3]
    f2_pages = Page.objects.all().filter(is_footer_2=True)[:3]
    f3_pages = Page.objects.all().filter(is_footer_3=True)[:3]

    context = {  
        'testmonials' : testmonials,
        'teams' : teams,
        'abouts':abouts,
        'slides':slides,   
        'services':services, 
        'heading':heading,
        'addresss':addresss,
        #'f1_pages':f1_pages,
        'f2_pages':f2_pages,
        'f3_pages':f3_pages,
        'photos': photos,
    }
    return render(request, 'pages/index.html', context)

@login_required
def central(request):
    subjects = Subject.objects.order_by('date_posted').filter(is_published=True)
    contactus = Contactus.objects.order_by('-contact_date')[:15]
    contact = Contact.objects.order_by('-contact_date')
    testmonials = Testmonial.objects.order_by('-contact_date')
    teachers = Teacher.objects.order_by('hire_date').filter(is_published=True)
    students = Student.objects.order_by('account_date').filter(is_published=True)
    parents = Parent.objects.order_by('account_date').filter(is_published=True)
    topics = Topic.objects.order_by('date_posted').filter(is_published=True)
    lessons = Lesson.objects.order_by('date_posted').filter(is_published=True)
    answers = Answer.objects.order_by('created_on')
    colors = Color.objects.all()[:1]
    customusers = CustomUser.objects.filter(is_active=True)
    exercises = Exercise.objects.order_by("-created_on").filter(is_published=True)[:10]
    todays = Today.objects.order_by('date_posted').filter(is_published=True)[:5]
    yesterdays = Today.objects.order_by('date_posted').filter(is_published=True)[:35]
    notices = Notice.objects.order_by('date_posted').filter(is_published=True)
    noticeg8 = Notice.objects.all().filter(is_grade8=True)
    noticeg7 = Notice.objects.all().filter(is_grade7=True)
    noticeg6 = Notice.objects.all().filter(is_grade6=True)
    noticeg5 = Notice.objects.all().filter(is_grade5=True)
    noticeg4 = Notice.objects.all().filter(is_grade4=True)
    noticeg3 = Notice.objects.all().filter(is_grade3=True)
    noticeg2 = Notice.objects.all().filter(is_grade2=True)
    noticeg1 = Notice.objects.all().filter(is_grade1=True)
    grades = Grade.objects.order_by('date_posted').filter(is_published=True)
    grade8 = Grade.objects.all().filter(is_grade8=True)
    grade7 = Grade.objects.all().filter(is_grade7=True)
    grade6 = Grade.objects.all().filter(is_grade6=True)
    grade5 = Grade.objects.all().filter(is_grade5=True)
    grade4 = Grade.objects.all().filter(is_grade4=True)
    grade3 = Grade.objects.all().filter(is_grade3=True)
    grade2 = Grade.objects.all().filter(is_grade2=True)
    grade1 = Grade.objects.all().filter(is_grade1=True)
    students8 = CustomUser.objects.filter(is_student=True).filter(is_grade8=True)
    students7 = CustomUser.objects.filter(is_student=True).filter(is_grade7=True)
    students6 = CustomUser.objects.filter(is_student=True).filter(is_grade6=True)
    students5 = CustomUser.objects.filter(is_student=True).filter(is_grade5=True)
    students4 = CustomUser.objects.filter(is_student=True).filter(is_grade4=True)
    students3 = CustomUser.objects.filter(is_student=True).filter(is_grade3=True)
    students2 = CustomUser.objects.filter(is_student=True).filter(is_grade2=True)
    students1 = CustomUser.objects.filter(is_student=True).filter(is_grade1=True)

    context = {
        'testmonials' : testmonials,
        'contact' : contact,
        'contactus' : contactus,
        'parents' : parents,
        'students': students,
        'teachers' : teachers,
        'students8' : students8,
        'students7' : students7,
        'students6' : students6,
        'students5' : students5,
        'students4' : students4,
        'students3' : students3,
        'students2' : students2,
        'students1' : students1,
        'customusers' : customusers,
        'answers': answers,
        'colors' : colors,
        'exercises' : exercises,
        'subjects' : subjects,
        'topics' : topics,
        'lessons': lessons,
        'todays' : todays,
        'yesterdays': yesterdays,
        'noticeg8' : noticeg8,
        'noticeg7' : noticeg7,
        'noticeg6' : noticeg6,
        'noticeg5' : noticeg5,
        'noticeg4' : noticeg4,
        'noticeg3' : noticeg3,
        'noticeg2' : noticeg2,
        'noticeg1' : noticeg1,
        'grades' : grades,
        'grade8' : grade8,
        'grade7' : grade7,
        'grade6' : grade6,
        'grade5' : grade5,
        'grade4' : grade4,
        'grade3' : grade3,
        'grade2' : grade2,
        'grade1' : grade1,

        
    }

    return render(request, 'pages/central.html', context )



