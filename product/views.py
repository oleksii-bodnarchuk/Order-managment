from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from product.forms import OrderForm

from product.models import Category, Product, Order


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    category_id = request.GET.get("category")
    if category_id:
        products = products.filter(category=category_id)
    return render(
        request,
        "product/product_list.html",
        {"products": products, "categories": categories},
    )


class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("product:product-list")
