from django.db import models

# Create your models here.
from django.db import models


class Poll(models.Model):
    poll_name = models.CharField(max_length=200)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    poll_description = models.CharField(max_length=250)

    def __str__(self):
        return self.poll_name


class Question(models.Model):
    poll_name = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text_question = models.CharField(max_length=200)
    # type 'text', 'one' or 'multiple'
    type_question = models.CharField(max_length=8)

    def __str__(self):
        return self.text_question[:50]


class Choice(models.Model):
    # id question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_choice = models.CharField(max_length=200)

    def __str__(self):
        return self.text_choice


class Answer(models.Model):
    user = models.IntegerField()
    poll_name = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll')
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    choice = models.ForeignKey(Choice, null=True,
                               on_delete=models.CASCADE,
                               related_name='choice')
    choice_type = models.CharField(max_length=8, null=True)

    def __str__(self):
        return self.choice_type
