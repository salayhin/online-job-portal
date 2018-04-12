from django import forms
from .models import Contract, Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )