
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


    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
