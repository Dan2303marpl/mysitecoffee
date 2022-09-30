from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def index(request):
    if request.method == "POST":
        form = request.POST
        print(form)
        user = authenticate(request,username=form['username'],password=form['password'])
        if user != None:
            return render(request,'authorization.html')
        else:
            return render(request,'notvalidname.html')


    return render(request,'authorization.html')




    
# Create your views here.
