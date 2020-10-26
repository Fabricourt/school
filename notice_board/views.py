from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from accounts.models import CustomUser
from .models import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.


class NoticeListView(ListView):
    model = Notice
    context_object_name = 'notices'
    ordering = ['-date_posted']
    paginate_by = 1

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['mvp_lessons'] = Lesson.objects.all().filter(is_mvp=True)
        context['topics'] = Topic.objects.all()
        return context


class NoticeDetailView(DetailView):
    model = Notice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['topics'] = Topic.objects.all()
        return context


class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notice
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == notice.created_by:
            return True
        return False


class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notice
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == notice.created_by:
            return True
        return False


class UserNoticeListView(ListView):
    model = Notice
    template_name = 'user_notices.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notices'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Notice.objects.filter(created_by=user).order_by('-date_posted')   
  
