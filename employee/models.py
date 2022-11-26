from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=256)
    inn = models.CharField(max_length=10)
    contact_fullname = models.CharField(max_length=256)
    contact_phone_number = models.CharField(max_length=16)


class Employee(AbstractUser):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    join_date = models.DateTimeField(null=True)
    exit_date = models.DateTimeField(null=True)
    fullname = models.CharField(max_length=256)
    date_of_birth = models.DateTimeField(null=True)
    position = models.CharField(max_length=256)
