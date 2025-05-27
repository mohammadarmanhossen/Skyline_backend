from rest_framework import serializers
from .models import District
from .import models

from rest_framework import serializers
from .models import Hotel,Order

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'district_name', 'slug']


class HotelSerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='district_names.district_name', read_only=True)
    district_names = serializers.PrimaryKeyRelatedField(queryset=District.objects.all(),write_only=True)

    class Meta:
        model = Hotel
        fields = [
            'id', 
            'hotel_name', 
            'address', 
            'district_names', 
            'district_name',  
            'image_url', 
            'description', 
            'price_per_night', 
            'available_room'
        ]



class BookedSerializer(serializers.ModelSerializer):
    hotel = serializers.CharField(source='hotel_name.hotel_name', read_only=True) 
    hotel_name = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all(), write_only=True)

    class Meta:
        model = models.Booked
        fields = ['id', 'hotel_name', 'hotel','room', 'in_date', 'out_date','total_amount', 'is_paid', 'is_failed', 'is_cencelled']
 



class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer): 

    class Meta:
        model = models.Review
        fields = ['id', 'rating','created', 'body']


