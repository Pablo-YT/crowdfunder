from django import forms
from django.forms import CharField, PasswordInput, ModelForm ,Form
from .models import Reward, Project


class LoginForm(forms.Form):
    username = CharField(label='User Name', max_length=64)
    password = CharField(widget=PasswordInput())


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        widget = {'end_at': forms.SelectDateWidget()}
        fields = [
            'title',
            'owner',
            'description',
            'funding_goal',
            'created_at',
            'end_at'
        ]

class RewardsForm(ModelForm):

    class Meta:
        model = Reward
        widgets = {'project': forms.HiddenInput()}
        fields = [
            'reward',
            'description',
            'level',
            'project'
        ]

