from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TaskSerializers

class TaskViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializers

