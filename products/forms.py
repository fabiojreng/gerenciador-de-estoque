from django import forms
from .models import Product
from django.utils.timezone import now


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            "title",
            "category",
            "brand",
            "description",
            "serie_number",
            "expiry_date",
            "cost_price",
            "selling_price",
            "quantity",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "brand": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "serie_number": forms.TextInput(attrs={"class": "form-control"}),
            "expiry_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "cost_price": forms.NumberInput(attrs={"class": "form-control"}),
            "selling_price": forms.NumberInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
        }
        labels = {
            "title": "Título",
            "category": "Categoria",
            "brand": "Marca",
            "description": "Descrição",
            "serie_number": "Número de Série",
            "expiry_date": "Data de Validade",
            "cost_price": "Preço de Custo",
            "selling_price": "Preço de Venda",
            "quantity": "Quantidade",
        }

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data.get("expiry_date")
        if expiry_date and expiry_date < now().date():
            raise forms.ValidationError(
                "A data de validade não pode ser anterior à data atual."
            )
        return expiry_date
