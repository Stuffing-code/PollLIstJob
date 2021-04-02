import logging
from datetime import datetime


from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import *

logger = logging.getLogger(__name__)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def poll_list_all(request):
    """Show all polls."""
    polls = Poll.objects.all()
    serializer = PollSerializers(polls, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def poll_list_active(request):
    """Show all active polls."""
    poll = Poll.objects.filter(date_end__gt=datetime.now()).filter(date_start__lte=datetime.now())
    serializer = PollSerializers(poll, many=True)
    return Response(serializer.data)


@api_view(['PATCH', 'DELETE'])
# @permission_classes((IsAdminUser, IsAuthenticated,))
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


@api_view(['POST'])
# @permission_classes((IsAdminUser, IsAuthenticated,))
def create_poll(request):
    serializer = PollSerializers(data=request.data, context={'request': request})
    if serializer.is_valid():
        poll = serializer.save()
        return Response(PollSerializers(poll).data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
# @permission_classes((IsAdminUser, IsAuthenticated,))
def create_question(request):
    serializer = QuestionSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        quest = serializer.save()
        return Response(QuestionSerializer(quest).data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PATCH', 'DELETE'])
# @permission_classes((IsAdminUser, IsAuthenticated,))
def delete_or_update_question(request, quest_id):
    quest = get_object_or_404(Question, pk=quest_id)
    if request.method == 'DElETE':
        quest.delete()
        return Response('Question deleted', status=204)
    elif request.method == 'PATCH':
        serializer = QuestionSerializer(quest, data=request.data, partial=True)
        if serializer.is_valid():
            quest = serializer.save()
            return Response(QuestionSerializer(quest).data)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
# @permission_classes((IsAdminUser, IsAuthenticated,))
def create_choice(request):
    serializer = ChoiceSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        choice = serializer.save()
        return Response(ChoiceSerializer(choice).data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PATCH', 'DELETE'])
# @permission_classes((IsAdminUser, IsAuthenticated,))
def delete_or_update_choice(request, choice_id):
    choice = get_object_or_404(Question, pk=choice_id)
    if request.method == 'DElETE':
        choice.delete()
        return Response('Question deleted', status=204)
    elif request.method == 'PATCH':
        serializer = ChoiceSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid():
            choice = serializer.save()
            return Response(ChoiceSerializer(choice).data)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def answer_create(request):
    serializer = AnswerSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        answer = serializer.save()
        return Response(AnswerSerializer(answer).data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def answer_view(request, user_id):
    answers = Answer.objects.filter(user_voter=user_id)
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)


@api_view(['PATCH', 'DELETE'])
# @permission_classes((IsAuthenticated, IsAdminUser,))
def delete_or_update_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'DELETE':
        answer.delete()
        return Response("Answer deleted", status=204)
    elif request.method == 'PATCH':
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            answer = serializer.save()
            return Response(AnswerSerializer(answer).data)
        return Response(serializer.errors, status=400)
