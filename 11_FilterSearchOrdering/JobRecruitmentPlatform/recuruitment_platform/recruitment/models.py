from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()
    
    def __str__(self):
        return self.name
    
class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    Company = models.ForeignKey(Company, related_name="jobs", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Applicant(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    resume = models.TextField()
    
    def __str__(self):
        return self.name
    
class Application(models.Model):
    applicant = models.ForeignKey(Applicant, related_name="applications", on_delete=models.CASCADE)
    job = models.ForeignKey(JobPosting, related_name="applications", on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('submitted', 'Submitted'),
        ('reviewing', 'Reviewing'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], default='submitted')
    
    class Meta:
        unique_together = ('applicant', 'job') # Can't apply to the same job twice
        
    def __str__(self):
        return f"{self.applicant.name} and {self.job.title}"
    