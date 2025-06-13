from django.contrib import admin
from .models import Company, JobPosting, Applicant, Application

# Register your models here.
admin.site.register(Company)
admin.site.register(JobPosting)
admin.site.register(Applicant)
admin.site.register(Application)
