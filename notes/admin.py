# Import necessary modules:
#    a. Import the admin module from django.contrib.
#    b. Import the Note model from the current package's models.
from django.contrib import admin

# Register your models here.
# Use the @admin.register(Note) decorator to register the Note model.
from .models import Note


@admin.register(Note)
# Define the NoteAdmin class:
#    a. Create a class NoteAdmin that inherits from admin.ModelAdmin.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
