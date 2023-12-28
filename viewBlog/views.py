from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogwrite.models import Blog


# Create your views here.

@login_required(login_url='login')
def view_blog(request):
    if request.method == 'POST':
        god_date = request.POST.get('date')
        print(f'date: {god_date} || type: {type(god_date)}')
        blogs = Blog.objects.filter(date=god_date)
        return render(request,'view_blog.html',{'blogs':blogs})
    else:
        return render(request,'view_blog.html')