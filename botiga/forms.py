from django import forms
from .models import Videojoc

class VideojocForm(forms.ModelForm):
    class Meta:
        model = Videojoc
        fields = ['titol', 'plataforma', 'preu', 'stock', 'venudes']
