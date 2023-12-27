from django.shortcuts import render,redirect
from .forms import BlogModelForm
from .models import Blog

# Create your views here.

def blogwrite(request):
    if request.method == 'POST':
        god_title = request.POST.get('title')
        god_content = request.POST.get('content')

        Blog.objects.create(title=god_title,content=god_content)
        return render(request,'blogwrite.html')


    return render(request,'blogwrite.html')