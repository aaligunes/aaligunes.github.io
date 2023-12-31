from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/home/1")
        
        else:
            return render (request, "account/login.html", {
                "error": "Kullancı adı ve/veya şifre yanlış !!!"
            } )
    
    return render(request,"account/login.html")

def register_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render (request, "account/register.html", {"error": "Kullanıcı adı mevcut lütfen farklı bir kullanıcı adı deneyiniz"})
            else:
                if User.objects.filter(email=email).exists():
                    return render (request, "account/register.html", {"error": "E-mail mevcut lütfen farklı bir kullanıcı adı deneyiniz"})
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    return redirect("login")
        else:
            return render (request, "account/register.html", {"error": "şifreler uyuşmuyor !!!"} )
    return render(request,"account/register.html")


  

def logout_request(request):
    logout(request)
    return redirect("/home/1")
