from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from django.db.models import Sum

class Project(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    funding_goal = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    end_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects', default=1)
    catagories = models.CharField(max_length=255, default='place')
    
    def current_funds(self):
       return self.backers.aggregate(Sum('amount_given'))['amount_given__sum']

    def dollars(self):
        dollars = self.funding_goal
        return "${:.2f}".format(dollars)
    

class Reward(models.Model):
    reward = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    level = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rewards')

class Backer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backer', default=1)
    amount_given = models.IntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='backers')
