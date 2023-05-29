from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/', views.category_api_view),
    path('api/categories/<int:id>/', views.category_detail_api_view),
    path('api/products/', views.products_api_view),
    path('api/products/<int:id>/', views.product_detail_api_view),
    path('api/reviews/', views.reviews_api_view),
    path('api/reviews/<int:id>/', views.review_detail_api_view)
]