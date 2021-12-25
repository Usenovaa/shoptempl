from django import forms
from mainapp.models import Product, Category, Image


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'descriptions', 'price', 'quantity', 'image', 'category',)

