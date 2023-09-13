from rest_framework import serializers
from .models import Todo

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title','todo_data','checked','date']