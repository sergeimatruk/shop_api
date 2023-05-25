from django.contrib import admin
from product.models import Category, Product, Review

admin.site.register(Category, Product, Review)