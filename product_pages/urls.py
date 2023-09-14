
from django.urls import path
from .views import all_products, shoping_card
urlpatterns = [
    path("product.html", all_products),
    path("shoping-cart.html", shoping_card, name='shoping_cart')
]
