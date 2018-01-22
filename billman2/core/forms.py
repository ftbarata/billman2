from django.forms import models
from django import forms
from .models import CustomerDetails


class ProfileForm(models.ModelForm):

    class Meta:

        model = CustomerDetails
        # fields = '__all__'
        exclude = ['email']

        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'id':'input_cpf'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'id': 'input_cnpj'}),
            'observations': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder':'Digite aqui qualquer tipo de informação adicional desejada.'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id':'id_nome'}),
            'razao_social': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_razao_social'}),
            'alternative_email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Opcional, mas desejável'}),
            'phones': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ex: (21) 999999999, (11) 88888888'}),
            'responsibles': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ex: João(Financeiro), José(Administrativo)'}),
        }