from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'category', 'priority', 'due_date', 'completed']
        read_only_fields = ['owner']


