from django import forms
from .models import Contract,Employee

class ContractForm(forms.ModelForm):
    class Meta:
        model=Contract
        fields = [
            'name',
            'email',
            'phone',
            'comment'
        ]

class EmployeeForm(forms.ModelForm):
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
        ]