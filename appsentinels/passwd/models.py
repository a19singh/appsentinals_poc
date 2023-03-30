from django.db import models
from django.utils import timezone

class PlatformUser(models.Model):
    """
    Model to keep and store passwords

    Attributes:
    -----------
       name: to store the name of user
       passwd: to store encrypted passwords
    """

    name = models.CharField(max_length=20, default='')
    passwd = models.CharField(max_length=100)
    cdate = models.DateTimeField(default=timezone.now) 
