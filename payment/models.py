from django.db import models

from hotels.models import Booked,Order



class Checkout(models.Model):
    booked = models.ForeignKey(Booked, on_delete=models.CASCADE, related_name="checkouts", default=1)  
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="checkouts", default=1)
    


    