from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

LOGIN = '/recipes/login/'
REGISTER = '/recipes/register/'
def login_page(request):
    if request.method != 'POST':
        return render(request, 'recipes/login.html', {"form_submitted": False})
    data = request.POST
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username = username, password = password)

    if user is None:
        messages.error(request, 'Invalid credentials!!')
    else:
        login(request, user)
        messages.info(request, 'Login successful')
        return redirect('/recipes/')
    return render(request, 'recipes/login.html', {"form_submitted": True})

def logout_page(request):
    logout(request)
    return redirect(LOGIN)

def register(request):
    if request.method == 'POST':
        return create_user(request)
    return render(request, 'recipes/register.html')

def create_user(request):
    data = request.POST
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    # check if username already exists, then throw an appropriate error
    has_username = User.objects.filter(username = username)
    if has_username.exists():
        messages.error(request, 'Username already taken!!')
        return redirect(REGISTER)
    password = data.get('password')
    user = User.objects.create(
        first_name = first_name,
        last_name = last_name,
        username = username,
    )
    user.set_password(password)
    user.save()
    messages.info(request, 'Account created successfully!!')
    return redirect(REGISTER)
