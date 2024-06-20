from django.apps import AppConfig


# Define the NotesConfig class:
#    a. Create a class NotesConfig that inherits from AppConfig.
class NotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes'
