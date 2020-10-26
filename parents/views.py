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

class ParentListView(ListView):
    model = Parent
    context_object_name = 'parents'
    ordering = ['-date_posted']
    paginate_by = 1

class UserParentListView(ListView):
    model = Parent
    template_name = 'user_parents.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'parents'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Parent.objects.filter(created_by=user).order_by('-date_posted')  
    


# Create your views here.
class ParentDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login'
    redirect_field_name = '/accounts/login'
    model = Parent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context




class ParentCreateView(LoginRequiredMixin, CreateView):
    model = Parent
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class ParentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Parent
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == parent.created_by:
            return True
        return False


class ParentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Parent
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == parent.created_by:
            return True
        return False
