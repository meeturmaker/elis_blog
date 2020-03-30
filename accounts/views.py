from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
  if request.method=='POST':
    username = request.POST["username"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]
    if password1==password2:
      if User.objects.filter(username=username).exists():
        messages.info(request,"Username taken")
        return redirect("register")
      elif User.objects.filter(email=email):
        messages.info(request,"email address is already used,please register with a different email address")
        return redirect("register")
          
      else:
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
        user.save()
        return redirect("login")
          
        
          
    else:
      messages.info(request,"passwords do not match")
      return redirect("register")

    # return redirect("/")
  else:
    return render(request,"register.html")



def login(request):
  if request.method=='POST':
    username = request.POST["username"]
    password = request.POST["password1"]
    user = auth.authenticate(username=username,password=password)

    if user is not None:
      auth.login(request,user)
      return redirect("/")
    else:
      messages.error(request, "login incorrect.Please try again")
      return redirect("login")

  return render(request,"login.html")

def logout(request):
  auth.logout(request)
  return redirect("/")