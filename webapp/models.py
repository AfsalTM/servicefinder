from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class signindb(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username  # Return the username for easier identification

class Service(models.Model):
    user = models.ForeignKey(signindb, on_delete=models.CASCADE, null=True)  # Link to signindb
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name  # Return the service name for easier identification