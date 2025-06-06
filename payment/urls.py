
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PaymentViewSet
from .views import get_order_by_booked

router = DefaultRouter()
router.register('checkout', views.CheckoutViewSet)
router.register('order', views.OrderViewSet)
router.register(r'payment', PaymentViewSet, basename='payment')


urlpatterns = [
    path('', include(router.urls)), 
     path("order/by-booked/<int:booked_id>/", get_order_by_booked),
    path('payment/success/', views.PaymentSuccessAPI.as_view(), name='payment_success'),  
    path('payment/failed/', views.PaymentFailedAPI.as_view(), name='payment_failed'),  
    path('payment/cancel/', views.PaymentCancelAPI.as_view(), name='payment_cancel'),   
]

