from django.shortcuts import render

from comunidad.models import Usuario

# Create your views here.
def usuario_list_view(request):
    titulo= "Usuarios"
    context={
        "titulo":titulo,
    }
    return render(request, 'admin/comunidad/usuarios.html', context)
