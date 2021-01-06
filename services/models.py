from django.db import models


class Service(models.Model):
    slug = models.SlugField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    des = models.CharField(max_length=500, blank=True, null=True)
    is_enrolled = models.BooleanField(null=True, blank=True, default=False)
    head1 = models.CharField(max_length=120, blank=True, null=True)
    desc1 = models.CharField(max_length=500, blank=True, null=True)
    head2 = models.CharField(max_length=120, blank=True, null=True)
    desc2 = models.CharField(max_length=500, blank=True, null=True)
    head3 = models.CharField(max_length=120, blank=True, null=True)
    desc3 = models.CharField(max_length=500, blank=True, null=True)
    buyLink = models.CharField(max_length=120, blank=True, null=True)
    img_card = models.ImageField(blank=True, null=True)
    img_main = models.ImageField(blank=True, null=True)
    def __str__(self):
        return str(self.name)
