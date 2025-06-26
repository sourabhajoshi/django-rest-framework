from django.contrib import admin
from .models.employee import Employee, Designation

admin.site.register(Employee)
admin.site.register(Designation)
