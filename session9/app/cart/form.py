# forms.py
from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    
class ProductForm(forms.Form):
	name = forms.CharField(max_length=200)
	price = forms.DecimalField(max_digits=10, decimal_places=2)