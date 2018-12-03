from django.contrib import admin

# Register your models here.

from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Department admin."""

    list_display = ('id', 'dep_description', 'fkdirection')