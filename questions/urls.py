from django.urls import path
from .views import ListAllQuestionsAPI, CreateQuestionAPI

urlpatterns = [
    path('list/', ListAllQuestionsAPI.as_view(), name='list_all'),
    path('create/', CreateQuestionAPI.as_view(), name='create'),
]
