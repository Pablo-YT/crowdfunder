"""crowdfunder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import root, project_view, project_create, project_show, login_view, logout_view, signup, catagorie_search, category, profile_show, category_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',root),
    path('projects/', project_view, name='project_view'),
    path('projects/create', project_create, name='project_create'),
    path('projects/<int:id>', project_show, name='project_show'),
    path('profile/<int:id>', profile_show, name='profile_show'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('search/', catagorie_search, name='catagorie_search'),
    path('category/', category_view, name='category_view'),
    path('category/<int:id>', category, name='category')
]
