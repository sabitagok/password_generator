from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'pass_generator/home.html')


def password_gen(request):
    length=int(request.GET.get('length'))
    alphabet= list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        alphabet.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        alphabet.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        alphabet.extend(list('0123456789'))
        
    password = ''
    for i in range(length):
        password+=random.choice(alphabet)
    return render(request, 'pass_generator/password_gen.html', {'PASSWORD': password})