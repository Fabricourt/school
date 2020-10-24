from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from accounts.models import CustomUser
from .models import Exercise, Answer
from grades.models import Grade
from subjects.models import *
from teachers.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class SubjectListView(ListView):
    model = Subject
    context_object_name = 'subjects'
    ordering = ['-date_posted']
    paginate_by = 1

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['mvp_lessons'] = Lesson.objects.all().filter(is_mvp=True)
        context['topics'] = Topic.objects.all()
        return context


class SubjectDetailView(DetailView):
    model = Subject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['topics'] = Topic.objects.all()
        return context


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class SubjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Subject
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == subject.created_by:
            return True
        return False


class SubjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Subject
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == subject.created_by:
            return True
        return False


class UserSubjectListView(ListView):
    model = Subject
    template_name = 'user_subjects.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'subjects'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Subject.objects.filter(created_by=user).order_by('-date_posted')   
  

#topics
class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    ordering = ['-date_posted']
    paginate_by = 1

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['mvp_lessons'] = Lesson.objects.all().filter(is_mvp=True)
        context['topics'] = Topic.objects.all()
        return context


class TopicDetailView(DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['topics'] = Topic.objects.all()
        return context


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TopicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Topic
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == topic.created_by:
            return True
        return False


class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Subject
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == topic.created_by:
            return True
        return False

class UserTopicListView(ListView):
    model = Subject
    template_name = 'user_topics.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'topics'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Topic.objects.filter(created_by=user).order_by('-date_posted')   
  

# lesson

class LessonListView(ListView):
    model = Topic 
    context_object_name = 'lessons'
    ordering = ['-date_posted']
    paginate_by = 100

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['mvp_lessons'] = Lesson.objects.all().filter(is_mvp=True)
        context['topics'] = Topic.objects.all()
        return context


class LessonDetailView(DetailView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customusers'] = CustomUser.objects.all()
        context['grades'] = Grade.objects.all()
        context['subjects'] = Subject.objects.all()
        context['topics'] = Topic.objects.all()
        context['lessons'] = Lesson.objects.all()
        context['exercises'] = Exercise.objects.filter(is_published=True).order_by("-created_on")
        context['grade8']  = Grade.objects.all().filter(is_grade8=True)
        context['grade7'] = Grade.objects.all().filter(is_grade7=True)
        context['grade6'] = Grade.objects.all().filter(is_grade6=True)
        context['grade5'] = Grade.objects.all().filter(is_grade5=True)
        context['grade4'] = Grade.objects.all().filter(is_grade4=True)
        context['grade3'] = Grade.objects.all().filter(is_grade3=True)
        context['grade2'] = Grade.objects.all().filter(is_grade2=True)
        context['grade1'] = Grade.objects.all().filter(is_grade1=True)
    
        return context

class LessonCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class LessonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lesson
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == lesson.created_by:
            return True
        return False


class LessonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lesson
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == lesson.created_by:
            return True
        return False

class UserLessonListView(ListView):
    model = Lesson
    template_name = 'user_lessons.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'lessons'
    paginate_by = 100

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Lesson.objects.filter(created_by=user).order_by('-date_posted')   
  
# Exercise
class ExerciseListView(generic.ListView):
    queryset = Exercise.objects.filter(is_published=True).order_by("-created_on")
    template_name = "exercise_list.html"
    paginate_by = 100


class ExerciseDetailView(generic.DetailView):
    model = Exercise
    template_name = 'exercise_detail.html'

class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ExerciseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Exercise
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == exercise.created_by:
            return True
        return False


class ExerciseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Exercise
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == exercise.created_by:
            return True
        return False


def exercise(request, slug):
    template_name = "exercise.html"
    exercise = get_object_or_404(Exercise, slug=slug)
    answers = exercise.answers.filter(active=True).order_by("-created_on")
    classes = Class.objects.order_by('class_name').filter(is_published=True)
    new_answer = None
    # answer exercise
    if request.method == "POST":
        answer_form = AnswerForm(request.POST, request.FILES)
        if answer_form.is_valid():
            # Create answer object but don't save to database yet
            new_answer = answer_form.save(commit=False)
            # Assign the current exercise to the answer
            new_answer.exercise = exercise

            new_answer.save()
    else:
        answer_form = AnswerForm()
    context = {
            "classes": classes,
            "exercise": exercise,
            "answers": answers,
            "new_answer": new_answer,
            "answer_form": answer_form,
    }
    return render(request, "exercises/exercise.html", context )

class UserExerciseListView(generic.ListView):

    model = Exercise
    template_name = 'exercises/user_exercises.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'exercises'
    paginate_by = 10

 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        context['students'] = Student.objects.all()
        return context

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
        return Exercise.objects.filter(teacher=user).order_by("-created_on") 

class UserAnswersListView(ListView):
    model = Exercise
    template_name = 'user_Answers.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Answers'
    paginate_by = 100

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Answer.objects.filter(created_by=user).order_by('-date_posted')  
          
# Answer
class AnswerListView(ListView):
    model = Answer
    template_name = 'answers/answers.html' 
    context_object_name = 'answers'
    ordering = ['-date_posted']
    paginate_by = 100

    


def answer(request, answer_id):
  answer = get_object_or_404(Answer, pk=answer_id)
  queryset = Exercise.objects.filter(status=1).order_by("-created_on")
  classes = Class.objects.order_by('class_name').filter(is_published=True)
  
  context = {
    'queryset': queryset,
    'answer': answer,
    "classes": classes,
  }
  return render(request, 'exercises/answer.html', context)


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = 'name, teacher, exercise, answers_typed'

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)
    

def answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    context = {
        'answer': answer
    }
    return render(request, 'exercises/answer.html', context)


class AnswerDetailView(DetailView):
    model = Answer


"""
class AnswerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Answer
    fields = '__all__'

    def form_valid(self, form):
        form.instance.name = self.request.user 
        return super().form_valid(form)

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.name: 
            return True
        return False
"""

class AnswerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Answer
    fields = '__all__'

    def form_valid(self, form):
        form.instance.teacher.name.first_name = self.request.user.first_name 
        return super().form_valid(form)

    def test_func(self):
        answer = self.get_object()
        if self.request.user.first_name == answer.teacher.name.first_name:
            return True
        return False

class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer
    success_url = 'central'

    def test_func(self):
        answer = self.get_object()
        if self.request.user.first_name == answer.teacher.name.first_name:
            return True
        return False

#todays
class TodayListView(ListView):
    model = Today 
    context_object_name = 'todays'
    ordering = ['-date_posted']
    paginate_by = 1

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['mvp_lessons'] = Lesson.objects.all().filter(is_mvp=True)
        context['topics'] = Topic.objects.all()
        return context


class TodayDetailView(DetailView):
    model = Today

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['topics'] = Topic.objects.all()
        return context


class TodayCreateView(LoginRequiredMixin, CreateView):
    model = Today
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TodayUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Today
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == today.created_by:
            return True
        return False


class TodayDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Today
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == today.created_by:
            return True
        return False

class UserTodayListView(ListView):
    model = Subject
    template_name = 'user_todays.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'todays'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Today.objects.filter(created_by=user).order_by('-date_posted')   
  
