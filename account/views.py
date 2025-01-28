from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.forms import MyUserCreationForm

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.success(request, "You have succesfully logged in.")
                next_url = request.POST.get("next")
                print(next_url)
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = AuthenticationForm()

        return render(request, 'account/login.html', {'form': form})
    else:
        return redirect('/')

@login_required(login_url=('account:login'))
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('/')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "You have successfully signed up and are now logged in.")
                return redirect("/")
            else:
                messages.error(request, "There was an error with your registration.")
        else:
            form = MyUserCreationForm()

        return render(request, "account/register.html", {"form": form})
