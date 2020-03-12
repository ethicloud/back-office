import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254)
    slug = models.CharField(max_length=254)

class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254)

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)

class Instance(models.Model):
    STATUS = (
        ('U', 'Up'),
        ('D', 'Down'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    status = models.CharField(max_length=1, choices=STATUS)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
