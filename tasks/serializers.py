from rest_framework import serializers
from tasks.models import Task
import users.serializers as usr

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = usr.UserSerializer()
    created_by = usr.UserSerializer()
    client = usr.ClientSerializer()
    class Meta:
        model = Task
        fields = '__all__'