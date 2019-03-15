from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Project, Reward
from .forms import RewardsForm, ProjectForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

def project_view(request):
    project = Project.objects.all()
    context = {
        'project': project
    }
    response = render(request, 'projectpage.html', context)
    return HttpResponse(response)
