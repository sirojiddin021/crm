from django.urls import path
from users.views import *


urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('users/<int:pk>/', UserAPIView.as_view()),
    path('get_me/', GetMe.as_view()),

    path('clients/', ClientAPIView.as_view()),
    path('clients/<int:pk>/', ClientDetailAPIView.as_view()),
]