from django.contrib.auth.models import User
from django.db import models


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    ph_no = models.IntegerField(blank=True, null=True, default=1234567891)
    height = models.IntegerField(blank=True, default=176)
    weight = models.IntegerField(blank=True, default=65)
    # profile_pic = models.ImageField(upload_to='/profile_photos')

    class Meta:
        db_table = "Extended Details"

    def __str__(self):
        return str(self.user.username)
