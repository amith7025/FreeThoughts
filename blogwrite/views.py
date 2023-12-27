from django.shortcuts import render

# Create your views here.

def blogwrite(request):
    return render(request,'blogwrite.html')