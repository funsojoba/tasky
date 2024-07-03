from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Task


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(many=True)
    class Meta:
        fields = '__all__'
        model = Task