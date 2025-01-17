from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples = [
        {'name': 'Varun', 'age': 18,},
        {'name': 'sanjana', 'age': 25}
    ]
    return render(request,"home/index.html", context={'peoples': peoples})