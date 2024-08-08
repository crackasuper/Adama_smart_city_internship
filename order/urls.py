
from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payment/<str:order_number>/', views.payment, name='payment'),
    path('dashboard',views.dashboard,name="dashboard"),
]
