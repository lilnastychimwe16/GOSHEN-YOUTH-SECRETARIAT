from django import forms
from .models import ZonalObligation, DistrictObligation

class ZonalObligationForm(forms.ModelForm):
    class Meta:
        model = ZonalObligation
        fields = ['category', 'current_figure', 'projected_target']
        widgets = {
            'current_figure': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'projected_target': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # If editing existing record
            self.fields['category'].widget.attrs['readonly'] = True
            self.fields['category'].widget.attrs['class'] = 'form-control-plaintext'

class DistrictObligationForm(forms.ModelForm):
    class Meta:
        model = DistrictObligation
        fields = ['district_name', 'current_figure', 'projected_target']
        widgets = {
            'current_figure': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'projected_target': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # If editing existing record
            self.fields['district_name'].widget.attrs['readonly'] = True
            self.fields['district_name'].widget.attrs['class'] = 'form-control-plaintext' 