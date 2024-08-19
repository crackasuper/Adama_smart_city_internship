
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('shop/', include("shop.urls")),
    path('carts/', include("carts.urls")),
    path('orders/',include("order.urls")),
    path('accounts/', include('django.contrib.auth.urls')), 

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
