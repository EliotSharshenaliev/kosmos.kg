
from django.urls import path
from .views import product_detail, all_products, shoping_card
urlpatterns = [
    path("product-detail.html", product_detail),
    path("product.html", all_products),
    path("shoping-cart.html", shoping_card)
]
