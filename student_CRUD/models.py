from django.db import models

# Create your models here.
class StudentDetail(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    course=models.CharField(max_length=50)
    enroll_date=models.DateField()
    def __str__(self):
        return self.name