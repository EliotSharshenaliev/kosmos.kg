from django.contrib import admin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.html import format_html
from django.views.generic import DetailView
from django.urls import path, reverse

from product_pages.models import Categorie, Product, PhotoProduct, Subcategorie, ColorsProduct, SizesProduct, Country, \
    Orderer, OrderItem


class SubCategoryAdmin(admin.StackedInline):
    model = Subcategorie


class SizesProductInline(admin.StackedInline):
    model = Product.size.through
    extra = 0
    min_num = 1


class ColorProductInline(admin.StackedInline):
    model = Product.color.through
    extra = 0
    min_num = 1


class PhotoProductInline(admin.StackedInline):
    model = Product.orderer.through
    extra = 0
    min_num = 1


class ProductStackedInline(admin.StackedInline):
    model = Product.orderer.through
    extra = 0
    min_num = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ColorProductInline, SizesProductInline]
    list_display = ('title', 'category', 'subcategory', 'price', 'currency', 'image_preview')

    def image_preview(self, obj):
        imagesContainer = ""
        for image in obj.photos.all():
            imagesContainer += f'<img src="{image.photo.url}" width="50" height="50" />'
        return format_html(imagesContainer) if obj.photos.exists() else ''

    image_preview.short_description = 'Image Preview'  # Column name


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "products.view_order"
    template_name = "admin/products/order/detail.html"
    model = Orderer

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **admin.site.each_context(self.request),
            "opts": self.model._meta,
        }


@admin.register(Orderer)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('firstname',
                    'lastname',
                    'detail',
                    'created'
                    )
    inlines = [OrderItemInline]

    def get_urls(self):
        return [
            path(
                "<pk>/detail",
                self.admin_site.admin_view(OrderDetailView.as_view()),
                name=f"products_order_detail",
            ),
            *super().get_urls(),
        ]

    def detail(self, obj: Orderer) -> str:
        url = reverse("admin:products_order_detail", args=[obj.pk])
        return format_html(f'<a href="{url}">Детальный просмотр заказа</a>')


admin.site.register(PhotoProduct)
admin.site.register(Product, ProductAdmin)
admin.site.register(Categorie)
admin.site.register(Subcategorie)
admin.site.register(SizesProduct)
admin.site.register(ColorsProduct)
admin.site.register(Country)
