from django.shortcuts import render
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import generics
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from .models import KeepNote
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class NoteView(APIView):
    """
        NoteView class performs all operations with methods defined under it
        methods: 
                get_note: Accept two types of request
                ```1 GET: List all notes created by an authenticated user
                ```2 POST: Allow authenticated user to create Note
                update_note: Allow authenticated user to update note that belong to them
    """
    @api_view(['GET', 'POST'])
    @permission_classes([IsAuthenticated])
    def get_note(request):
        """
           get_note: Accept two types of request
                ```1 GET: List all notes created by an authenticated user
                ```2 POST: Allow authenticated user to create Note
        """
        user_id = request.user.id
        notes = KeepNote.objects.filter(user_id=user_id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    @api_view(['PUT'])
    @permission_classes([IsAuthenticated])
    def update_note(request, id):
        """
        Update note by using the note Id in the database and
        ensure proper validation before saving to the database
        """
        try:
            user_id = request.user.id
            note = KeepNote.objects.get(id=id)
            if note.user_id != user_id:
                return Response({"Message": "Not allow"}, 400)

            title = request.POST.get('title')
            content = request.POST.get('content')
            # Updated Fields
            note.title = title
            note.content = content
            serializer = NoteSerializer(note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({"message": "Item does not exists"}, 403)

    @api_view(['DELETE'])
    @permission_classes([IsAuthenticated])
    def delete_note(request, id):
        """
            delete note by using its Id in the database
            Note: check the "view.py" file
        """
        try: 
            user_id = request.user.id
            note = KeepNote.objects.get(id=id)
            if note.user_id == user_id:
                note.delete()
                return Response({"message": "Deleted successfully"})
            else:
                return Response({"message": "Priviledge not given"})
        except ObjectDoesNotExist:
                return Response({"message": "Object not found"})
