import json
from django.shortcuts import render
from django.http import JsonResponse
#dj rest
from rest_framework.response import Response
from rest_framework.decorators import api_view 
#models and serialzers
from .models import Note
from .serializers import NoteSerializer
# Create your viewshere.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)
    #safe means we can return more data than python dictionart

@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all()
    serializer=NoteSerializer(notes,many=True) 
    #many =T for multiple objects and F for single object
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,note_id):
    try:
        note=Note.objects.get(id=note_id) 
    except:
        return Response('404')
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)