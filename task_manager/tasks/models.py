from django.db import models
from django.contrib.auth.models import User

def get_default_user():
  return User.objects.first().id # Returns the first user in the database

class Task(models.Model):
  STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
  ]

  title = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  due_date = models.DateField()
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
  user = models.ForeignKey(User, on_delete=models.CASCADE) # Each task belongs to a single user

  def __str__(self):
    return self.title