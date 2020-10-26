from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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

def teachers(request):
  teachers = Teacher.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(teachers, 25)
  page = request.GET.get('page')
  paged_teachers = paginator.get_page(page)

  context = {
    'teachers': paged_teachers
  }

  return render(request, 'teachers/teachers.html', context)

def teacher(request, teacher_id):
  teacher = get_object_or_404(Teacher, pk=teacher_id)

  context = {
    'teacher': teacher
  }

  return render(request, 'teachers/teacher.html', context)




# Create your views here.
class TeacherDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login'
    redirect_field_name = '/accounts/login'
    model = Teacher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context

class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teachers'
    ordering = ['-date_posted']
    paginate_by = 100

class UserTeacherListView(ListView):
    model = Teacher
    template_name = 'user_teachers.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'teachers'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Parent.objects.filter(created_by=user).order_by('-date_posted')  
    


# Create your views here.
class TeacherDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login'
    redirect_field_name = '/accounts/login'
    model = Teacher

  




class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class TeacherUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Teacher
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == teacher.created_by:
            return True
        return False


class TeacherDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Teacher
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == teacher.created_by:
            return True
        return False
