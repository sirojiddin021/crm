from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task
from django.shortcuts import get_object_or_404
from tasks.serializers import TaskSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class TaskAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(tags=['tasks'])
    def get(self, request):
        if request.user.is_manager:
            tasks = Task.objects.all()
            ser = TaskSerializer(tasks, many=True)
            return Response(ser.data)
        else:
            tasks = Task.objects.filter(assigned_to=request.user)
            ser = TaskSerializer(tasks, many=True)
            return Response(ser.data)
        
    @swagger_auto_schema(request_body=TaskSerializer, tags=['tasks'])
    def post(self, request):
        if request.user.is_manager:
            task = TaskSerializer(data=request.data)
            if task.is_valid():
                task.save()
                return Response(task.data)
            return Response(task.errors)
        return Response({'message':'not allowed'})
    

class TaskDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['tasks'])
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        ser = TaskSerializer(task)
        return Response(ser.data)
    
    @swagger_auto_schema(request_body=TaskSerializer,tags=['tasks'])
    def patch(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        if request.user == task.assigned_to:
            updated = TaskSerializer(data=request.data, instance=task, partial=True)
            if updated.is_valid():
                updated.save()
                return Response(updated.data)
            return Response(updated.errors)
        return Response({'message':'not allowed'})
   
    @swagger_auto_schema(tags=['tasks'])
    def delete(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return Response({'message':'deleted'})
    

class DeleteAPIView(APIView):
    @swagger_auto_schema(tags=['tasks'], request_body=TaskSerializer)
    def post(self, request):
        tasks = request.data
        for task in tasks:
            Task.objects.filter(id=task['id']).delete()
        return Response({'message':'deleted'})
