from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class PilotProgram(models.Model):
    title = models.CharField(max_length=80)
    quick_description = models.CharField(max_length=200)
    full_description = models.TextField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}: {self.quick_description}"


class Task(models.Model):
    name = models.CharField(max_length=120)
    description =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_at = models.DateField()
    complete = models.BooleanField(default=False)
    pilot_program = models.ForeignKey(PilotProgram, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"{self.name}"