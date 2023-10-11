from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['image'].required = False

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']
        labels = {'name': '', 'description': '', 'price': '', 'quantity': '', 'image': ''}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование товара'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание товара'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

