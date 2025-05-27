
from django.shortcuts import render
from rest_framework import viewsets
from .import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .import serializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response



from rest_framework import viewsets
from .models import Booked,Order
from .serializer import BookedSerializer



class DistrictViewSet(viewsets.ModelViewSet):
    queryset=models.District.objects.all()
    serializer_class=serializer.DistrictSerializer
    lookup_field = 'slug'

class HotelViewSet(viewsets.ModelViewSet):
    queryset=models.Hotel.objects.all()
    serializer_class=serializer.HotelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['district_names']
    search_fields = ['hotel_name'] 
    permission_classes = [AllowAny] 

    def destroy(self, request, *args, **kwargs):
        hotel = self.get_object()
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookedViewSet(viewsets.ModelViewSet):
    queryset = Booked.objects.all()
    serializer_class = BookedSerializer





class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializer.OrderSerializers



class ReviewViewSet(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializer.ReviewSerializer

    