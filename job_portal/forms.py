from django import forms
from .models import Contract

class contract_form(forms.ModelForm):
    class Meta:
        model=Contract
        fields = [
            'name',
            'email',
            'phone',
            'comment'
        ]