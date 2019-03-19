from django.contrib import admin
from .models import Project, Reward, Backer, Category

admin.site.register(Project)
admin.site.register(Reward)
admin.site.register(Backer)
admin.site.register(Category)
