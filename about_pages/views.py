from django.shortcuts import render


def about(request):
    return render(request=request, template_name="about.html")
