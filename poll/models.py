from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db import models


class Poll(models.Model):
    poll_name = models.CharField(max_length=200)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    poll_description = models.TextField(max_length=800)

    def __str__(self):
        return f'{self.poll_name}, {self.poll_description}'


class Question(models.Model):
    TEXT = 'TEXT'
    CHOICE = 'CHOICE'
    MULTIPLE = 'MULTIPLE'

    choices = (
        (TEXT, 'TEXT'),
        (CHOICE, 'CHOICE'),
        (MULTIPLE, 'MULTIPLE'),
    )
    poll_name = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text_question = models.CharField(max_length=200)
    type_question = models.CharField(max_length=8, choices=choices, default=TEXT)

    def __str__(self):
        return self.text_question[:50]


class Choice(models.Model):
    # id question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, default='Enter value')

    def __str__(self):
        return self.value


class UserVoter(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'


class Answer(models.Model):
    user_voter = models.ForeignKey(UserVoter, related_name='answers', on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user_voter} value: {self.value}'
