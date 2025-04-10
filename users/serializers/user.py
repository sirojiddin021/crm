from rest_framework import serializers
import users.models as models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['first_name', 'last_name', 'username', 'password', 'is_manager']
        extra_kwargs = {'password': {'write_only':True}}
        
    def create(self, validated_data):
        password = validated_data['password']
        user = models.CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user