from django import forms

from accounts.models import *


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nome', 'prenom' , 'tel' , 'adress' ]

class LivarisonForm(forms.ModelForm):
    class Meta:
        model = Livraison
        fields = ['libelle', 'date']