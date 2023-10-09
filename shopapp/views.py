from datetime import date, timedelta

from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, render

from shopapp import models as shopapp_models
from shopapp.forms import ProductForm


def product_list(request, customer_id, days):
    customer = get_object_or_404(shopapp_models.Customer, pk=customer_id)
    startdate = date.today() + timedelta(days=1)
    enddate = startdate - timedelta(days=days)

    orders = customer.orders.filter(created__range=[enddate, startdate])
    products = set(order.product for order in orders)

    return render(request, "shopapp/product_list.html", {"products": products, "days": days})


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            if image is None:
                FileSystemStorage().save(image.name, image)
            form.save(commit=True)
    else:
        form = ProductForm()

    return render(request, "shopapp/create_form.html", {"form": form})
