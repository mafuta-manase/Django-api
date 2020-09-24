from django.db import models

# Create your models here.

class Contacts(models.Model):
    first_name    = models.CharField(max_length=100, blank=False,null=False)
    last_name    = models.CharField(max_length=100, blank=False,null=False)
    email   = models.EmailField()
    address = models.CharField(max_length=250, blank=True, null=True)
    phone   = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name