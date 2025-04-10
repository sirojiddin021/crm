from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
import users.models as models
import users.serializers as sers


class ClientAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(tags=['clients'])
    def get(self, request):
        clients = models.Client.objects.all()
        ser = sers.ClientSerializer(clients, many=True)
        return Response(ser.data)
    
    @swagger_auto_schema(tags=['clients'], request_body=sers.ClientSerializer)
    def post(self, request):
        client = sers.ClientSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response(client.data)
        return Response(client.errors)
    

class ClientDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['clients'])
    def get(self, request, pk):
        client = get_object_or_404(models.Client, id=pk)
        ser = sers.ClientSerializer(client)
        return Response(ser.data)
    
    @swagger_auto_schema(tags=['clients'], request_body=sers.ClientSerializer)
    def patch(self, request, pk):
        client = get_object_or_404(models.Client, id=pk)
        updated = sers.ClientSerializer(data=request.data, instance=client, partial=True)
        if updated.is_valid():
            updated.save()
            return Response(updated.data)
        return Response(updated.errors)
    
    @swagger_auto_schema(tags=['clients'])
    def delete(self, request, pk):
        client = get_object_or_404(models.Client, id=pk)
        client.delete()
        return Response({'message':'deleted'})
    

class DeleteAPIView(APIView):
    @swagger_auto_schema(tags=['users'], request_body=sers.ClientSerializer)
    def post(self, request):
        clients = request.data
        for client in clients:
            models.CustomUser.objects.filter(id=client['id']).delete()
        return Response({'message':'deleted'})