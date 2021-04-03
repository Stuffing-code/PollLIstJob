from rest_framework import serializers
from .models import *


class PollSerializers(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'text_question', 'poll_name', 'type_question']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'value']
        read_only_fields = ['id']


class AnswerSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'questions', 'user_voter', 'choice', 'value']
        read_only_fields = ['id']


class UserVoterSerializers(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = UserVoter
        fields = ['id', 'poll', 'user', 'choice', 'answers']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        answers = validated_data.pop('answers', [])
        instance = UserVoter.objects.create(**validated_data)
        Answer.objects.bulk_create([
            Answer(vote=instance, **attr) for attr in answers
        ])
        return instance
