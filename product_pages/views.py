from django.shortcuts import render
from product_pages.models import Categories, Product, PhotoProduct


def all_products(request):
    categories_queryset = Categories.objects.all()
    products = Product.objects.prefetch_related('photos')
    context = {
        'products': products,
        "categories": categories_queryset
    }

    return render(request=request, template_name="product.html", context=context)


def product_detail(request):
    return render(request=request, template_name="product-detail.html")


def shoping_card(request):
    return render(request=request, template_name="shoping-cart.html")
