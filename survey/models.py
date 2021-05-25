from django.db import models
from django.conf import settings


class Polls(models.Model):
    name = models.CharField(max_length=100)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    description = models.CharField(max_length=200)

    def __str__(self):
        if self.name is None:
            return "ERROR NAME IS NULL"
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Polls, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    question_type = models.CharField(max_length=100)

    def __str__(self):
        return self.poll


class Choices(models.Model):
    question_choice = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_choice


class Answer(models.Model):
    user_answer_id = models.IntegerField()
    poll = models.ForeignKey(Polls, related_name='poll', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question',on_delete=models.CASCADE)
    choice = models.ForeignKey(Choices, related_name='choice', on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.choice_text
