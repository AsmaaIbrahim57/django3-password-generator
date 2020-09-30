from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    generatedPassword=""
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length'))
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+-')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    for i in range(length):
        generatedPassword+=random.choice(characters)
    
    return render(request,'generator/passwordPage.html',{'password':generatedPassword})
