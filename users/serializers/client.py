from rest_framework import serializers
import users.serializers.user as usr
import users.models as models


class ClientSerializer(serializers.ModelSerializer):
    created_by = usr.UserSerializer()
    created_by_id = serializers.PrimaryKeyRelatedField(queryset=models.CustomUser.objects.all(), source='created_by')
    class Meta:
        model = models.Client
        fields = '__all__'