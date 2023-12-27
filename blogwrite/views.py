from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BlogModelForm
from .models import Blog
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def blogwrite(request):
    if request.method == 'POST':
        god_title = request.POST.get('title')
        god_content = request.POST.get('content')

        if god_title == '' or god_content == '':
            return HttpResponse('404! error one of the field is empty')

        Blog.objects.create(title=god_title,content=god_content)
        return render(request,'home.html')


    return render(request,'blogwrite.html')
