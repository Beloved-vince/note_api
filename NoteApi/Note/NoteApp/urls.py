from . import views
from django.urls import path

urlpatterns = [
    path("notes/", views.NoteView.get_note),
    path("delete-note/<int:id>", views.NoteView.delete_note),
    path('update-note/<int:id>', views.NoteView.update_note),
]