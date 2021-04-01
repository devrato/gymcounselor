from django.db import models


class Service(models.Model):
    slug = models.SlugField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    des = models.CharField(max_length=500, blank=True, null=True)
    is_enrolled = models.BooleanField(null=True, blank=True, default=False)
    buyLink = models.CharField(max_length=120, blank=True, null=True)
    img_card = models.ImageField(blank=True, null=True)
    img_first = models.ImageField(blank=True, null=True)
    test_l1 = models.CharField(max_length=120, blank=True, null=True)
    test_l2 = models.CharField(max_length=120, blank=True, null=True)
    test_l3 = models.CharField(max_length=120, blank=True, null=True)
    test_n1 = models.CharField(max_length=120, blank=True, null=True)
    test_n2 = models.CharField(max_length=120, blank=True, null=True)
    test_n3 = models.CharField(max_length=120, blank=True, null=True)
    test_d1 = models.CharField(max_length=450, blank=True, null=True)
    test_d2 = models.CharField(max_length=450, blank=True, null=True)
    test_d3 = models.CharField(max_length=450, blank=True, null=True)
    feat_l = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return str(self.name)
