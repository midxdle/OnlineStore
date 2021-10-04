from django.http.response import HttpResponse
from .models import *
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
# Create your views here.




@csrf_exempt    
def home(request):
    data = Fruit.objects.all()
    size = len(data)
    if size>=3:
        context = {
            'fruits':[
                {
                    'name': data[0].name,
                    'price' : data[0].price,
                    'img' : data[0].image
                },
                {
                    'name': data[1].name,
                    'price' : data[1].price,
                    'img' : data[1].image
                },
                {
                    'name': data[2].name,
                    'price' : data[2].price,
                    'img' : data[2].image
                },
            ]
        }
    elif size==2:
        context = {
            'fruits':[
                {
                    'name': data[0].name,
                    'price' : data[0].price,
                    'img' : data[0].image
                },
                {
                    'name': data[1].name,
                    'price' : data[1].price,
                    'img' : data[1].image
                },
            ]
        }
    elif size==1:
        context = {
            'fruits':[
                {
                    'name': data[0].name,
                    'price' : data[0].price,
                    'img' : data[0].image
                },
            ]
        }
    else:
        return HttpResponse('database is empty. please add fruit',status =400)
    return render(request,'home.html',context= context)

def menu(request):
    fruits = Fruit.objects.all()
    vegtabales = Vegtabale.objects.all()
    context = {
        'fruits' : fruits,
        'vegtabales' : vegtabales,
    }
    return render(request,'menu.html',context=context)



def logpage(request):
    return render(request,'login.html')



def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'login.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('blog:home')
        else:
            return render (request,'login.html', {'error':'Password does not match!'})
    else:
        return render(request,'login.html')



def login(request):
    if request.method == 'POST':
        user = User.objects.filter(username=request.POST['username']).first()
        print('user : ',user)
        if user.check_password(request.POST['password']):
            auth.login(request,user)
            return redirect('blog:home')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'blog:home')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')