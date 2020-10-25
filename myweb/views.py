from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout as logout_user

def index(request):
    return render(request,'myweb/index.html')

def login_active(req):
    if req.method =="POST":
        Username = req.POST.get("username")
        Password = req.POST.get("password")
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(req, user)
            return render(req,'myweb/home.html')

def login_page(req):
    return render(req,'myweb/login.html')

def logout(req):
    logout_user(req)
    return redirect('login')
def home(request):
    return render(request,'myweb/home.html')
def GarnierMen(request):
    return render(request,'myweb/GarnierMen.html')
def Men(request):
    return render(request,'myweb/Men.html')
def niveacreme(request):
    return render(request,'myweb/niveacreme.html')
def pag(request):
    return render(request,'myweb/pag.html')
def pag100(request):
    return render(request,'myweb/pag100.html')
def pag100_1(request):
    return render(request,'myweb/pag100_1.html')
def pag100_2(request):
    return render(request,'myweb/pag100_2.html')
def pag200(request):
    return render(request,'myweb/pag200.html')
def pag200_1(request):
    return render(request,'myweb/pag200_1.html')
def pag200_2(request):
    return render(request,'myweb/pag200_2.html')
def sejan(request):
    return render(request,'myweb/sejan.html')
def SK(request):
    return render(request,'myweb/SK.html')
def sum150(request):
    return render(request,'myweb/sum150.html')
def sum200(request):
    return render(request,'myweb/sum200.html')
def ta100(request):
    return render(request,'myweb/ta100.html')
def ta100_1(request):
    return render(request,'myweb/ta100_1.html')
def ta100_2(request):
    return render(request,'myweb/ta100_2.html')
def ta200(request):
    return render(request,'myweb/ta200.html')
def ta200_1(request):
    return render(request,'myweb/ta200_1.html')
def ta200_2(request):
    return render(request,'myweb/ta200_2.html')
def Tros(request):
    return render(request,'myweb/Tros.html')
def Wa100(request):
    return render(request,'myweb/Wa100.html')
def Wa100_1(request):
    return render(request,'myweb/Wa100_1.html')
def Wa100_2(request):
    return render(request,'myweb/Wa100_2.html')
def Wa200(request):
    return render(request,'myweb/Wa200.html')
def Wa200_1(request):
    return render(request,'myweb/Wa200_1.html')
def Wa200_2(request):
    return render(request,'myweb/Wa200_2.html')
def Women(request):
    return render(request,'myweb/Women.html')
def wpag100(request):
    return render(request,'myweb/wpag100.html')
def wpag100_1(request):
    return render(request,'myweb/wpag100_1.html')
def wpag100_2(request):
    return render(request,'myweb/wpag100_2.html')
def wpag200(request):
    return render(request,'myweb/wpag200.html')
def wpag200_1(request):
    return render(request,'myweb/wpag200_1.html')
def wpag200_2(request):
    return render(request,'myweb/wpag200_2.html')
def wpom100(request):
    return render(request,'myweb/wpom100.html')
def wpom100_1(request):
    return render(request,'myweb/wpom100_1.html')
def wpom100_2(request):
    return render(request,'myweb/wpom100_2.html')
def wpom200(request):
    return render(request,'myweb/wpom200.html')
def wpom200_1(request):
    return render(request,'myweb/wpom200_1.html')
def wpom200_2(request):
    return render(request,'myweb/wpom200_2.html')
def wsum150(request):
    return render(request,'myweb/wsum150.html')
def wsum150_1(request):
    return render(request,'myweb/wsum150_1.html')
def wsum150_2(request):
    return render(request,'myweb/wsum150_2.html')
def wsum200(request):
    return render(request,'myweb/wsum200.html')
def wsum200_1(request):
    return render(request,'myweb/wsum200_1.html')
def wsum200_2(request):
    return render(request,'myweb/wsum200_2.html')
def wta100(request):
    return render(request,'myweb/wta100.html')
def wta100_1(request):
    return render(request,'myweb/wta100_1.html')
def wta100_2(request):
    return render(request,'myweb/wta100_2.html')
def wta200(request):
    return render(request,'myweb/wta200.html')
def wta200_1(request):
    return render(request,'myweb/wta200_1.html')
def wta200_2(request):
    return render(request,'myweb/wta200_2.html')
def Wwa100(request):
    return render(request,'myweb/Wwa100.html')
def Wwa100_1(request):
    return render(request,'myweb/Wwa100_1.html')
def Wwa100_2(request):
    return render(request,'myweb/Wwa100_2.html')
def Wwa200(request):
    return render(request,'myweb/Wwa200.html')
def Wwa200_1(request):
    return render(request,'myweb/Wwa200_1.html')
def Wwa200_2(request):
    return render(request,'myweb/Wwa200_2.html')
