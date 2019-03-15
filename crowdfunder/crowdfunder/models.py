from django.db import models
from datetime import datetime, date

class Project(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    funding_goal = models.IntegerField()
    created_at = models.DateTimeField() #now
    end_at = models.DateTimeField()

class Reward(models.Model):
    reward = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    level = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rewards')

    
