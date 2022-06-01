from django.db import models

# Create your models here.
class Jobs(models.Model):
    job_title=models.CharField(max_length=120)
    company_name=models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    salary=models.IntegerField(null=0)
    experience=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title