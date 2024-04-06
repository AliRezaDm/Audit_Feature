
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    #all auth
    path('', include('allauth.urls')),
    # My models 
    path('', include('goods.urls')), 
    path('cart', include('cart.urls'))
]


urlpatterns += static(settings.MEDIA_URL, 	document_root=settings.MEDIA_ROOT)