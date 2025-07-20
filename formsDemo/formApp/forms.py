from django import forms

class EmployeInfoForm(forms.Form):
    name = forms.CharField()
    salary = forms.IntegerField()