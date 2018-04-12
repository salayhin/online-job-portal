from django import forms
from .models import Contract,Employee

class contract_form(forms.ModelForm):
    class Meta:
        model=Contract
        fields = [
            'name',
            'email',
            'phone',
            'comment'
        ]

class employee_form(forms.ModelForm):
    class Meta:
        model=Employee
        fields = [
            'name',
            'fathers_name',
            'mothers_name',
            'present_address',
            'permanent_address',
            'picture',
            'gender',
            'age',
            'phone',
            'email',
            'nationality',
            'national_id',
            'skills',
            'religion',
            'sex',
            'marital_status',
            'created_at',
            'updated_at'
        ]