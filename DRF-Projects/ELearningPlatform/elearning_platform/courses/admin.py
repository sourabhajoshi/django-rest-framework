from django.contrib import admin
from .models import Instructor, Course, Student, Enrollment, Lesson
from django.apps import apps

# admin.site.register(Instructor)
# admin.site.register(Course)

app = apps.get_app_config('courses')

for model in app.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
        