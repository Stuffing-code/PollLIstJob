from datetime import datetime

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK

from .serializers import *


@api_view(['GET'])
def login(request):

    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def poll_list_all(request):
    """Show all polls."""
    polls = Poll.objects.all()
    serializer = PollSerializers(polls, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def poll_list_active(request):
    """Show all active polls."""
    poll = Poll.objects.filter(date_end__gt=datetime.now()).filter(date_start__lte=datetime.now())
    serializer = PollSerializers(poll, many=True)
    return Response(serializer.data)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAdminUser, IsAuthenticated,))
def delete_or_update_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'DElETE':
        poll.delete()
        return Response('Poll deleted', status=204)
    elif request.method == 'PATCH':
        serializer = PollSerializers(poll, data=request.data, partial=True)
        if serializer.is_valid():
            poll = serializer.save()
            return Response(PollSerializers(poll).data)
        return Response(serializer.errors, status=400)
