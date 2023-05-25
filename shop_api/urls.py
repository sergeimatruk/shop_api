from django.contrib import admin
from django.urls import path
from django.conf.urls import static
from shop_api import settings
from product.views import category_list_api_view, category_retrieve_api_view, product_list_api_view, product_retrieve_api_view, review_list_api_view, review_retrieve_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/categories', category_list_api_view),
    path('/categories/<int:id>/', category_retrieve_api_view),
    path('/products', product_list_api_view),
    path('/products/<int:id>/', product_retrieve_api_view),
    path('/reviews', review_list_api_view),
    path('/reviews/<int:id>/', review_retrieve_api_view)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
