from django.shortcuts import render

# Create your views here.

def login_check(request):
    return render(request,'login.html')