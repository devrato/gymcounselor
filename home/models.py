from django.db import models
from datetime import datetime, timedelta
# Create your models here.
class Contact(models.Model):
    dateandtime = models.DateTimeField(default=datetime.now())
    phone_number = models.CharField(max_length=12)