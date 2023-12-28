from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_check(request):
    # print("Inside login_check view")
    if request.method == 'POST':
        username = 'God'  # Replace this with a more secure method to retrieve the username
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        # Debugging: Print or log information about the user object
        # print(f'user: {user}')
        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')  # Make sure you have a URL named 'dashboard'
        else:
            # Provide a more informative error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
