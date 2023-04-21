from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import Todo
from djoser.serializers import UserCreateSerializer


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'datetime', 'body', 'completed_task']


class MyUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ["id", "email", "password", "first_name", "last_name", "username"]
