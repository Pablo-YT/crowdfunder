from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Project, Reward
from .forms import RewardsForm, ProjectForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


def root(request):
    return HttpResponseRedirect('/projects')

def project_view(request):
    project = Project.objects.all()
    context = {
        'project': project
    }
    response = render(request, 'projectpage.html', context)
    return HttpResponse(response)

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = form.instance
            new_project.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm()
    html_response = render(request, 'projectcreate.html', {'form': form})
    return HttpResponse(html_response)

def project_show(request, id):
    project = Project.objects.get(pk=id)
    reward = project.rewards.all()
    if request.method == 'POST':
        rewards_form = RewardsForm(request.POST)
        if rewards_form.is_valid():
            new_reward = rewards_form.save()
            return HttpResponseRedirect('/projects/{}'.format(id))
        else:
            # put some errors
            pass
    else:
        rewards_form = RewardsForm(initial={'project': id})
    context = {
        'project': project,
        'reward': reward,
        'rewards_form': rewards_form
    }
    response = render(request, 'projectshow.html', context)
    return HttpResponse(response)

# def project_rewards(request, id):
#     project = Project.objects.get(pk=id)
#     if request.method == 'POST':
#         rewards_form = RewardsForm(request.POST)
#         if rewards_form.is_valid():
#             new_reward = rewards_form.save()
#             new_reward.save()
#             return HttpResponseRedirect('/projects/{}'.format(id))
#         else:
#             # need errors prob
#             pass
#     else:
#         rewards_form = RewardsForm(initial={'project': id})
#     context = {
#         'rewards_form': rewards_form,
#         'project': project
#     }
#     response = render(request, 'placeholder.html', context)
#     return HttpResponse(response)
