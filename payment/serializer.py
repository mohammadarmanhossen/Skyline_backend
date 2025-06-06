from rest_framework import serializers
from .models import Checkout,Order



class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
    
    


class CheckoutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"

