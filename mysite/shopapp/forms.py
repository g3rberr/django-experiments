from django import forms
from django.core import validators

from shopapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'discount')


from django.contrib.auth.models import Group
from django.forms import ModelForm

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name',)