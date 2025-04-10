from django.urls import path
from tasks.views import *

urlpatterns = [
    path('tasks/', TaskAPIView.as_view()),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view()),
    path('tasks/delete/', DeleteAPIView.as_view()),
]