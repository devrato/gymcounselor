from django.contrib.auth.models import User
from django.db import models


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    ph_no = models.CharField(max_length=10, blank=True, null=True)
    height = models.IntegerField(blank=True, default=176)
    weight = models.IntegerField(blank=True, default=65)

    class Meta:
        db_table = "Extended Details"

    def __str__(self):
        return str(self.user.username)
