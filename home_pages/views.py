from django.shortcuts import render


def home(request):
    return render(request=request, template_name="home.html")


def home2(request):
    return render(request=request, template_name="home-02.html")


def home3(request):
    return render(request=request, template_name="home-03.html")
