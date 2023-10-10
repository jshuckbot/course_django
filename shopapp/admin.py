from django.contrib import admin

from shopapp import models as shopapp_models


@admin.register(shopapp_models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "total", "created"]
    list_filter = ["name", "created"]
    list_editable = ["price"]


@admin.register(shopapp_models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email", "phone", "address"]
    list_filter = ["first_name", "created"]


@admin.register(shopapp_models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "product", "total_price", "created"]
    list_filter = ["total_price", "created"]
    raw_id_fields = ["customer", "product"]
