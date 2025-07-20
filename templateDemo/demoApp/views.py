from django.shortcuts import render
import datetime

# Create your views here.

def display(request):
    date = datetime.datetime.now()
    message = ''
    hour = int(date.strftime('%H'))
    if hour < 12:
        message += 'Good Morning'
    else:
        message += 'Good Evening'
    name = 'Selva'
    date_dict = {'display_date': date, 'empname': name, 'greetings': message}
    return render(request, 'demoApp/abc.html', context = date_dict)