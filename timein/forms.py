from django import forms
from .models import Student
from timein.choices import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('ID_number', 'first_name', 'last_name', 'course', 'purpose','pc',)
        widgets = {
        'ID_number': forms.TextInput(attrs={'placeholder': 'ID number','class': 'form-control', 'id': 'id', }),
        'first_name': forms.TextInput(attrs={'placeholder': 'First name','class': 'form-control', 'id': 'fname'}),
        'last_name': forms.TextInput(attrs={'placeholder': 'Last name','class': 'form-control','id': 'lname'}),
        'course': forms.TextInput(attrs={'placeholder': 'Course', 'class': 'form-control','id': 'course'}),
        'pc':forms.NumberInput(attrs={'placeholder': 'PC number', 'class': 'form-control', 'id': 'pc', 'type': 'number'}),
        'purpose':forms.Select(attrs={'class': 'form-control custom-select', 'id': 'purpose',}),
        }
class lout(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('timeout',)
        widgets = {
            'timeout':forms.TimeInput(attrs={'class': 'form-control'}),
            }