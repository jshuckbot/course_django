from django import forms

from shopapp import models as shopapp_models


class ProductForm(forms.ModelForm):
    class Meta:
        model = shopapp_models.Product
        fields = ["name", "description", "price", "image", "total"]
