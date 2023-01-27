from django.urls import path

from product.views import product_list, OrderCreateView


urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("order/create/", OrderCreateView.as_view(), name="order-create"),
]

app_name = "product"
