from datetime import date, timedelta

from django.shortcuts import get_object_or_404, render

from shopapp import models as shopapp_models


def product_list(request, customer_id, days):
    customer = get_object_or_404(shopapp_models.Customer, pk=customer_id)
    startdate = date.today() + timedelta(days=1)
    enddate = startdate - timedelta(days=days)

    orders = customer.orders.filter(created__range=[enddate, startdate])
    products = set(order.product for order in orders)

    return render(request, "shopapp/product_list.html", {"products": products, "days": days})
