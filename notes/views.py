from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .models import Post
from .forms import NoteForm
from .forms import PostForm


# Define the note_list view function:
# Define a function note_list that takes a request object as a parameter.
# Query all Note objects and store them in the variable notes.
# Render the 'notes/note_list.html' template with the context {'notes': notes}.
# Return the rendered template as the response.
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


# Define the note_detail view function:
# Define a function note_detail that takes a request object and a primary key (pk) as parameters.
# Use get_object_or_404 to get the Note object with the given pk and store it in the variable note.
# Render the 'notes/note_detail.html' template with the context {'note': note}.
# Return the rendered template as the response.
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


# Define the note_create view function:
# Define a function note_create that takes a request object as a parameter.
# Check if the request method is 'POST':
#       i. Create a NoteForm instance with the POST data.
#       ii. Check if the form is valid:
#          - Save the form data to create a new Note object.
#          - Redirect to the 'note_list' URL.
# If the request method is not 'POST':
#       i. Create an empty NoteForm instance.
# Render the 'notes/note_form.html' template with the context {'form': form}.
# Return the rendered template as the response.
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'notes/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'notes/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'notes/post_form.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'notes/post_form.html', {'form': form})
