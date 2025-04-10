from django.db import models
from users.models import CustomUser, Client

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='task')
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_tasks')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=[('1', 'new'), ('2', 'in_progress'), ('3', 'completed')])
    deadline = models.DateField()