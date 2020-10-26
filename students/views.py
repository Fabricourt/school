from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from accounts.models import CustomUser
from .models import *
from students.models import Student
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    ordering = ['-date_posted']
    paginate_by = 1

class UserStudentListView(ListView):
    model = Student
    template_name = 'user_students.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'students'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Student.objects.filter(created_by=user).order_by('-date_posted')  
    


# Create your views here.
class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login'
    redirect_field_name = '/accounts/login'
    model = Student




class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == student.created_by:
            return True
        return False


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == student.created_by:
            return True
        return False
