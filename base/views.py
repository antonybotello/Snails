from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def index_admin(request):
    titulo="Inicio"
    context={
        "titulo":titulo,
    }
    return render(request,"index-admin.html",context)

def index_user(request):
    titulo="Inicio"
    context={
        "titulo":titulo,
    }
    return render(request,"index-user.html",context)

def logout_user(request):
    logout(request)
    return redirect('index-user')