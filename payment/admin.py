from django.contrib import admin
from .models import Checkout
from .models import Order

admin.site.register(Checkout)
admin.site.register(Order)