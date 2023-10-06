from django.urls import path

from shopapp import views

urlpatterns = [
    path("product_list/<int:customer_id>/<int:days>", views.product_list, name="product_list"),
    # path("about/", views.about_me, name="about"),
]
