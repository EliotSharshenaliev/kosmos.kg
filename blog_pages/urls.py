
from django.urls import path
from .views import blog, blog_detail

urlpatterns = [
    path("blog.html", blog),
    path("blog-detail.html", blog_detail)
]
