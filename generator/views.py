from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def password(request):

    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ""

    lenght = int(request.GET.get('lenght'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))

    if request.GET.get('symbols'):
        characters.extend(list('+-*/.<>,_!"#$%&()=¡@|°}{?¨´]['))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for i in range(lenght):
        generated_password += random.choice(characters)
    
    return render(request, 'password.html', {'password': generated_password})