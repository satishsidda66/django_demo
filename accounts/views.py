from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):

 if request.method == 'POST':

    username = request.POST['username']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    repassword = request.POST['repassword']
    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'username already exists')
            print("username already exists")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists')
            print("email already exists")

        else:
            user = User.objects.create_user(
                username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            user.save()
            messages.info(request, 'registration successful')
    else:
        messages.info(request, 'password not matching')

    return redirect('/accounts')
 else:
     return render(request, 'register.html')


def login(request):
   if request.method == 'POST':

    username = request.POST['username']

    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    print("saasasassa", user)

    if user is not None:
        auth.login(request, user)
        return render(request, 'dashboard.html', {'username': username})
    else:
        messages.info(request, 'invalid cerdentials')
        return redirect('/accounts')
   else:
    return render(request,'login.html')
