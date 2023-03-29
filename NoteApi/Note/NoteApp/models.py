from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class KeepNote(models.Model):
    """
    Args:
        title: Title of the note with maximum of 100 chars
        content: Of the note
        date_created: Automatically created
        date_updated: Automatically updated
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return the title of the note only"""
        return self.title