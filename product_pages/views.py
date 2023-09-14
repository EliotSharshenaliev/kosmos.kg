import json
from django.shortcuts import redirect
from django import forms
from django.shortcuts import render
from product_pages.models import Categorie, Product, Country, Orderer, OrderItem


def all_products(request):
    categories_queryset = Categorie.objects.all()
    products = Product.objects.all()
    context = {
        'products': products,
        "categories": categories_queryset,
        'products_json': products,
    }

    return render(request=request, template_name="product.html", context=context)


class OrderForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'stext-111 cl8 plh3 size-111 p-lr-15', 'placeholder': 'Имя'}))
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'stext-111 cl8 plh3 size-111 p-lr-15', 'placeholder': 'Фамилия'}))
    number_phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'stext-111 cl8 plh3 size-111 p-lr-15', 'placeholder': 'Номер телефона'}))
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        initial=Country.objects.first(),
        widget=forms.Select(attrs={'class': 'js-select2', 'name': 'country'}))

    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'stext-111 cl8 plh3 size-111 p-lr-15', 'placeholder': 'Город'}))
    store_location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'stext-111 cl8 plh3 size-111 p-lr-15', 'placeholder': 'Адресс/ТЦ'}))
    store = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'stext-111 cl8 plh3 size-111 p-lr-15', 'placeholder': 'Магазин (не обязательно)'}))

    orders = forms.CharField(widget=forms.Textarea(attrs={'style': "display: none"}))


def shoping_card(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                orders = form.cleaned_data.pop("orders")
                # county = form.cleaned_data.pop("country")
                orders = json.loads(orders)
                orderer = Orderer.objects.create(
                    **form.cleaned_data,
                )
                orderer.save()
                for order in orders:
                    product = Product.objects.get(pk=order.get("productId"))
                    OrderItem(
                        order=orderer,
                        product=product,
                        count=int(order.get("countAddBasked", 0))
                    ).save()

                form = OrderForm()
                return redirect("product.html")
            except json.JSONDecodeError as e:
                return render(request=request, template_name="shoping-cart.html", context={'form': form})
    else:
        form = OrderForm()
    return render(request=request, template_name="shoping-cart.html", context={'form': form})
