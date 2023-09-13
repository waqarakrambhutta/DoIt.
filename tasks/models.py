from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    todo_data = models.CharField(max_length=255)
    checked = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.title