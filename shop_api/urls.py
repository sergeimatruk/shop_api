from django.conf.urls.static import static
from shop_api import settings
from django.urls import path, include

urlpatterns = [

    path('api/v1/', include('shop_api.urls')),
    path('api/v1/users/', include('users.urls'))

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)