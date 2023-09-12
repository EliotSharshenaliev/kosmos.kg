from django.contrib import admin

from product_pages.models import Categories, Product, PhotoProduct


class PhotoProductAdmin(admin.StackedInline):
    model = PhotoProduct


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoProductAdmin]

    class Meta:
        model = Product


admin.site.register(PhotoProduct)
admin.site.register(Product, ProductAdmin)
admin.site.register(Categories)
