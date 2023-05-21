from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin





class CustomUserLogin(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('notepadapp:note_list')
    

class CustomLogoutView(LoginRequiredMixin,LogoutView):
    template_name = 'registration/logout.html'
    

class Notes_List(LoginRequiredMixin,ListView):
    model = Note
    template_name = "notepadapp/note_list"
    paginate_by = 10
    ordering = ['-created_date']
    context_object_name = "notes"
    
    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

class Create_Notes(LoginRequiredMixin,CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notepadapp/note_create.html"
    success_url = reverse_lazy('notepadapp:note_list')



    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    


class Update_Notes(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notepadapp/note_update.html"
    success_url = reverse_lazy('notepadapp:note_list')
    context_object_name = 'note'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        note = self.get_object() 
        return note.author == self.request.user
    

class Detail_Notes(LoginRequiredMixin,DetailView):
    model = Note
    template_name = "notepadapp/note_detail.html"
    context_object_name = "note"
    
    
class Delete_Notes(LoginRequiredMixin,DeleteView):
    model = Note
    template_name = "notepadapp/note_delete.html"
    context_object_name = 'note'
    success_url = reverse_lazy('notepadapp:note_list')

    def test_func(self):
        note = self.get_object()
        return note.author == self.request.user

        
    
    
        