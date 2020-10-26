from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    print()
    contact = Contact( name=name, email=email, message=message )
    contact.save()
    messages.success(request, 'Submitted Successfully')
    
    return redirect('index')
   
class ContactusDetailView(DetailView):
    model = Contactus


class ContactusCreateView(LoginRequiredMixin, CreateView):
    model = Contactus
    fields = '__all__'

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)



class TestmonialCreateView(LoginRequiredMixin, CreateView):
    model = Testmonial
    success_url = '/'
    success_message = "Your feedback has been submitted   successfully"
    fields = [
                'parent_name', 
                'message',

            ]

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class TestmonialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Testmonial
    fields = '__all__'
    success_url = '/central'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_admin:
            return True
        return False


   
