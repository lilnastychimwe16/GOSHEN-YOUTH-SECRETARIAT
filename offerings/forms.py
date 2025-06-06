from django import forms
from .models import FreewillOffering

class FreewillOfferingForm(forms.ModelForm):
    class Meta:
        model = FreewillOffering
        fields = ['amount', 'week_start_date']
        widgets = {
            'week_start_date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        } 