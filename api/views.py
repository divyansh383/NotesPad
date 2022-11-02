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
    notes=Note.objects.all().order_by('-updated')
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

@api_view(['PUT'])
def updateNote(request,note_id):
    data=request.data
    note=Note.objects.get(id=note_id)
    serialiser=NoteSerializer(instance=note,data=data)

    if(serialiser.is_valid()):
        serialiser.save()

    return Response(serialiser.data)

@api_view(['DELETE'])
def deleteNote(request,note_id):
    note=Note.objects.get(id=note_id)
    note.delete()
    return Response('Note deleted')

@api_view(['POST'])
def createNote(request):
    data=request.data
    note=Note.objects.create(body=data['body'])
    try:
        note.title=data['title']
    except:
        note.title="__none__"
        print("no title---------------------------------------",note)

    serialiser=NoteSerializer(data=note,many=False)
    if(serialiser.is_valid()):
        serialiser.save()
    return Response(serialiser.data)
    