from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Note
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(NoteForm, self).__init__(*args, **kwargs)

    # def save(self,commit=True):
    #     # if self.instance.user:
    #     #     self.user = self.user
    #     # else:
    #     #     self.user = self.instance.user
    #         return super(NoteForm, self).save(commit=commit)
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance
        

        


