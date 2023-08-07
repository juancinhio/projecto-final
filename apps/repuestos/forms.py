from django import forms
from .models import Repuestos

class RepuestosForm(forms.ModelForm):
    class Meta:
        model = Repuestos
        fields = ['afinacion', 'frenos', 'suspencion', 'service', 'embrague', 'distribucion', 'circuito_refrigerante', 'electricidad', 'motor', 'otros']