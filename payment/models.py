from django.db import models
from django.contrib.auth.models import User
from hotels.models import Booked
from hotels.models import Hotel

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    zip_code = models.CharField(max_length=10)


class Checkout(models.Model):
    booked = models.ForeignKey(Booked, on_delete=models.CASCADE, related_name="checkouts", default=1)  
    is_paid = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    is_failed = models.BooleanField(default=False)
    order = models.OneToOneField("Order", on_delete=models.SET_NULL, null=True, blank=True, related_name="order")



    