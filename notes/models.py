from django.db import models

# Create your models here.
from django.utils import timezone


# Define the Note model:
# Create a class Note that inherits from models.Model.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Define the string representation method:
    # Define the __str__ method to return the title of the note.
    def __str__(self):
        return self.title
