from django.shortcuts import render
import random
from django.http import HttpResponse


# def home(request):
#     return HttpResponse('<h1>This definately is my Home Page!</h1>')

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):



    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('!"£$%^&*@')
    if request.GET.get('numbers'):
        characters.extend('1234567890')

    length = int(request.GET.get('length',12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})