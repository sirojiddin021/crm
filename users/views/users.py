from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from users.permissions import IsManager
from django.shortcuts import get_object_or_404
import users.serializers as sers
import users.models as models


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated, IsManager]
    @swagger_auto_schema(tags=['users'])
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(models.CustomUser, id=pk)
            ser = sers.UserSerializer(user)
            return Response(ser.data)
        users = models.CustomUser.objects.all()
        ser = sers.UserSerializer(users, many=True)
        return Response(ser.data)
    
    @swagger_auto_schema(tags=['users'], request_body=sers.UserSerializer)
    def post(self, request):
        user = sers.UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.errors)
    

class GetMe(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(tags=['users'])
    def get(self, request):
        user = sers.UserSerializer(request.user)
        return Response(user.data)
    

class DeleteAPIView(APIView):
    @swagger_auto_schema(tags=['users'], request_body=sers.UserSerializer)
    def post(self, request):
        users = request.data
        for user in users:
            models.CustomUser.objects.filter(id=user['id']).delete()
        return Response({'message':'deleted'})