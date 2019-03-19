from django import forms
from django.forms import CharField, PasswordInput, ModelForm ,Form
from .models import Reward, Project, Backer


class LoginForm(forms.Form):
    username = CharField(label='User Name', max_length=64)
    password = CharField(widget=PasswordInput())


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        widgets = {'end_at': forms.SelectDateWidget(), 'owner': forms.HiddenInput(), 'created_at': forms.HiddenInput()}
        fields = [
            'title',
            'owner',
            'description',
            'funding_goal',
            'created_at',
            'end_at',
            'catagories'
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


class BackersForm(ModelForm):

    class Meta:
        model = Backer
        widgets = {'project': forms.HiddenInput(), 'user': forms.HiddenInput()}
        fields = [
            'user',
            'amount_given',
            'project'
        ]

