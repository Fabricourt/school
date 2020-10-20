from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404 
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import *
from services.models import *
from contacts.models import Contact_heading, Address
from home.models import Slide, Page

# Create your views here.
class AboutDetailView(DetailView):
    model = About

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.order_by("date_posted").filter(is_published=True)
        context['mvp_teams'] = Team.objects.all().filter(is_mvp=True)[:1]
        context['staff_teams'] = Team.objects.all().filter(is_staff=True)
        context['services'] = Service.objects.order_by("date_posted").filter(is_published=True)
        context['solutions'] = Solution.objects.order_by("date_posted").filter(is_published=True)
        context['addresss'] = Address.objects.all() 
        context['f1_pages'] = Page.objects.all().filter(is_footer_1=True)[:3]
        context['f2_pages'] = Page.objects.all().filter(is_footer_2=True)[:3]
        context['f3_pages'] = Page.objects.all().filter(is_footer_3=True)[:3]
       
        return context
