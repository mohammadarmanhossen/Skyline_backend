
from django.shortcuts import render
from rest_framework import viewsets
from .import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .import serializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response



from rest_framework import viewsets
from .models import Booked
from .serializer import BookedSerializer



from rest_framework.pagination import PageNumberPagination

class HotelPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50



class DistrictViewSet(viewsets.ModelViewSet):
    queryset=models.District.objects.all()
    serializer_class=serializer.DistrictSerializer
    lookup_field = 'slug'

class HotelViewSet(viewsets.ModelViewSet):
    queryset=models.Hotel.objects.all()
    serializer_class=serializer.HotelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['district_names__district_name', 'hotel_name']
    permission_classes = [AllowAny] 
    pagination_class = HotelPagination

    


    def destroy(self, request, *args, **kwargs):
        hotel = self.get_object()
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookedViewSet(viewsets.ModelViewSet):
    queryset = Booked.objects.all()
    serializer_class = BookedSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializer.ReviewSerializer

    