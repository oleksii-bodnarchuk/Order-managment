from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from product.models import User, Category, Product, Order

admin.site.register(User, UserAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "get_category", "user", "price"]
    search_fields = ["price"]

    @admin.display(ordering='category__name', description='Category')
    def get_category(self, obj):
        return obj.category.name


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "get_product", "get_category", "get_price"]
    search_fields = ["product"]

    @admin.display(ordering='product__name', description='Product')
    def get_product(self, obj):
        return obj.product.name

    @admin.display(ordering='product__category__name', description='Category')
    def get_category(self, obj):
        return obj.product.category.name

    @admin.display(ordering='product__price', description='Price')
    def get_price(self, obj):
        return obj.product.price
