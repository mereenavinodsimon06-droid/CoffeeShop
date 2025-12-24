from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import MenuItem,Order

def home(request):
    return render(request, 'coffee/home.html')

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'coffee/menu.html', {'items': items})

def my_order(request):
    return render(request, 'coffee/order.html')

@login_required
def place_order(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)

    Order.objects.create(
        user=request.user,
        item=item
    )

    return redirect('my_order')    

def about(request):
    return render(request, 'coffee/about.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "coffee/signup.html")

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "coffee/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'coffee/login.html')

