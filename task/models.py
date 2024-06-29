import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def get_id():
    return uuid.uuid4().hex



class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=get_id, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=(
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Overdue', 'Overdue')
    ))
    priority = models.CharField(max_length=100, choices=(
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ))
    due_date = models.DateTimeField()
    category = models.CharField(max_length=100)
    assigned_to = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    