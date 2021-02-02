from django.db import models
from datetime import datetime, timedelta
# Create your models here.


class Order(models.Model):
    order_id = models.CharField(max_length=50)
    razorpay_payment_id = models.CharField(max_length=50)
    service_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    oder_date = models.DateTimeField(default=datetime.now())
    expiry_date = models.DateTimeField(
        default=datetime.now()+timedelta(days=30))

    def __str__(self):
        return self.order_id
