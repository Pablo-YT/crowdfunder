from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Project, Reward, User, Backer, Category
from .forms import RewardsForm, ProjectForm, LoginForm, BackersForm
from django.contrib.auth import authenticate, login, logout
from crowdfunder.forms import LoginForm
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
            new_project.user = request.user
            new_project.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm()
    html_response = render(request, 'projectcreate.html', {'form': form})
    return HttpResponse(html_response)

def project_show(request, id):
    project = Project.objects.get(pk=id)
    reward = project.rewards.all()
    backer = project.backers.all()
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
    if request.method == 'POST': #comnbine the if statments
        backer_form = BackersForm(request.POST)
        if backer_form.is_valid():
            new_backer = backer_form.save()
            return HttpResponseRedirect('/projects/{}'.format(id))
        else:
            # put some errors
            pass
    else:
        backer_form = BackersForm(initial={'project': id, 'user': request.user})
    context = {
        'project': project,
        'backer': backer,
        'reward': reward,
        'rewards_form': rewards_form,
        'backer_form': backer_form,
    }
    response = render(request, 'projectshow.html', context)
    return HttpResponse(response)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/projects/')
            else:
                form.add_error('username', 'Login Failed')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    response = render(request, 'login.html', context)
    return HttpResponse(response)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/projects/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/projects/')
    else:
        form = UserCreationForm()
    html_response = render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response)


def catagorie_search(request):
    query = request.GET['query']
    search_result = Project.objects.filter(catagories__icontains=query)
    context = {
        'search_result': search_result,
        'query': query
    }
    response = render(request, 'search.html', context)
    return HttpResponse(response)

def profile_show(request, id):
    return render(request, 'profile.html', {
        'user': User.objects.get(pk=id)
    })


def categories(request):
    category = Category.objects.all()
    context = {'category': category}
    response = render(request, 'category.html', context)
    return HttpResponse(response)


def profile(request):
    return render(request, 'users/profile.html')
