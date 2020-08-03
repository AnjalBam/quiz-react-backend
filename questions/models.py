from django.db import models


class Question(models.Model):
    q_title = models.CharField(max_length=200)


class Answer(models.Model):
    answer_no = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answers')
    choice_answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
