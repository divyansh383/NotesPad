from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes,name='getRoutes'),
    path('notes/',views.getNotes,name='notes'),
    path('note/create',views.createNote,name='create-note'),
    path('note/<str:note_id>/update',views.updateNote,name='update-note'),
    path('note/<str:note_id>/delete',views.deleteNote,name='delete-note'),
    path('note/<str:note_id>',views.getNote,name='note'),
    
]
