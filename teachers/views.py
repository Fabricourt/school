from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *

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