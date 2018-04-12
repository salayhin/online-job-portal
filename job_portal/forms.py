from django import forms
from .models import Contract,Employee,EmployeeExperience,EmployeeEducation,EmployeeJob
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



class EmployeeEducationForm(forms.ModelForm):
    class Meta:
        model=EmployeeEducation
        fields = [
            'employee',
            'exam',
            'session',
            'passing_year',
            'result',
            'board',
            'university',
            'subject'

        ]


class EmployeeExperinenceForm(forms.ModelForm):
    class Meta:
        model = EmployeeExperience
        fields = [
            'emp_education',
            'job_title',
            'company_name',
            'start_date',
            'end_date'
        ]

class EmployeeJobForm(forms.ModelForm):
    class Meta:
        model = EmployeeJob
        fields = [
            'job',
            'employee',
            'expected_salary',
            'cover_letter'
        ]
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

