from django.shortcuts import render


def blog(request):
    return render(request=request, template_name="blog.html")


def blog_detail(request):
    return render(request=request, template_name="blog-detail.html")
