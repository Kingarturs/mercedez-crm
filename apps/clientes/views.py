from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def login_view(request):
    form = AuthenticationForm()
    if request.user.is_authenticated:
        return redirect("/menu")

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/menu')
        else:
            messages.error(request, "Usuario y/o contraseña incorrectos")
    return render(request, 'login.html', {'form': form})

def login_method(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/admin")

def logout_method(request):
    logout(request)
    return redirect('/')

def admin_view(request):
    if request.user.is_authenticated:

        user = User.objects.filter(username=request.user).first()

        if user.tipo == "SE":
            return render(request, "menuEmpleado.html", {"User": request.user})
        else:
            return render(request, "menuAdmin.html", {"User": request.user})
    else:
        return redirect("/")