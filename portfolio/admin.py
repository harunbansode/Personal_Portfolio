from django.contrib import admin
from .models import Project_details

@admin.register(Project_details)
class Project_detailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'year']