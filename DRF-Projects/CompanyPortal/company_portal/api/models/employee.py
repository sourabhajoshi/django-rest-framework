from django.db import models

class Designation(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title
    

class Employee(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    date_joined = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name