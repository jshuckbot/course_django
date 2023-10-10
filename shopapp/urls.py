from django.urls import path

from shopapp import views

urlpatterns = [
    path("product_list/<int:customer_id>/<int:days>", views.product_list, name="product_list"),
    path("create_product/", views.product_create, name="product_create"),
    # path("about/", views.about_me, name="about"),
]
