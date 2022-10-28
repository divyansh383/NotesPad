from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes,name='getRoutes'),
    path('notes/',views.getNotes,name='notes'),
    path('note/<str:note_id>',views.getNote,name='note')
]
