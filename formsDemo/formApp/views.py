from django.shortcuts import render
from . import forms

# Create your views here.

def empDetailsView(request):
    form = forms.EmployeInfoForm()
    empInfo = {'form': form}
    return render(request, 'formApp/index.html', context = empInfo)