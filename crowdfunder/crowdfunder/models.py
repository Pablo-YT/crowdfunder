from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.validators import MinValueValidator, MaxValueValidator

min_value = MinValueValidator(0,'Please Enter A Value Higher Than Zero.')

class Project(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    funding_goal = models.IntegerField(validators=[min_value])
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    end_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects', default=1)
    catagories = models.CharField(max_length=255, default='place')
    
    def current_funds(self):
        amount = self.backers.aggregate(Sum('amount_given'))['amount_given__sum']
        if amount == None:
            amount = 0
        return "${:.2f}".format(amount)
    

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
    amount_given = models.IntegerField(validators=[min_value])
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='backers')
