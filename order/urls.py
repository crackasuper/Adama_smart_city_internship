
from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payment/<str:order_number>/', views.payment, name='payment'),
    #path('dashboard',views.dashboard,name="dashboard"),
    #path('order-complete/', views.order_complete, name='order_complete'),
    #path('dashboard/',views.dashboard, name='dashboard'),
    path('chapa_payment/<int:order_number>/', views.chapa_payment, name='chapa_payment'),
    path('payment_verify/', views.chapa_payment_verify, name='chapa_payment_verify'),
]
