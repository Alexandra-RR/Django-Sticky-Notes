# notes/forms.py
from django import forms
from .models import Note
from .models import Post


# Define the NoteForm class:
#    a. Create a class NoteForm that inherits from forms.ModelForm.
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
