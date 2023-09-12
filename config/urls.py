
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home_pages.urls")),
    path('', include("about_pages.urls")),
    path('', include("contacts_pages.urls")),
    path('', include("blog_pages.urls")),
    path('', include("product_pages.urls")),
    path('', lambda request: redirect("home.html")),
]
