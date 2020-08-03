from django.shortcuts import render
# from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from .seriralizers import QuestionSerializer, Question


class ListAllQuestionsAPI(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class CreateQuestionAPI(CreateAPIView):
    serializer_class = QuestionSerializer


