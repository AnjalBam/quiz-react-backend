from django.shortcuts import render
# from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from .seriralizers import QuestionSerializer, Question
from .pagination import MyPageNumberPagination


class ListAllQuestionsAPI(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    pagination_class = MyPageNumberPagination


class CreateQuestionAPI(CreateAPIView):
    serializer_class = QuestionSerializer


