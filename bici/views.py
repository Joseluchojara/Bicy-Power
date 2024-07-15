from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bicicleta, Cliente
from .forms import ClienteForm
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'bici/index.html', context)

def nosotros(request):
    context = {}
    return render(request, 'bici/nosotros.html', context)

def inicio(request):
    context = {}
    return render(request, 'bici/inicio.html', context)

def tienda(request):
    context = {
        'productos': [
            {'nombre': 'Bicicleta Oxford', 'precio': 1000, 'imagen': 'img/bicicleta1.jpg'},
            {'nombre': 'Bicicleta Scott', 'precio': 1200, 'imagen': 'img/bicicleta2.jpg'},
            {'nombre': 'Bicicleta Trek', 'precio': 1500, 'imagen': 'img/bicicleta3.jpg'}
        ]
    }
    return render(request, 'bici/tienda.html', context)

@login_required
def sesion(request):
    request.session["usuario"] = request.user.username
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'bici/menu.html', context)

def accesorios(request):
    context = {}
    return render(request, 'bici/accesorios.html', context)


def API(request):
    context = {}
    return render(request, 'bici/API.html', context)

def list(request):
    clientes = Cliente.objects.all()  # Obtener todos los clientes de la base de datos

    context = {
        'clientes': clientes,  # Pasar los clientes al contexto
    }
    return render(request, 'bici/list.html', context)

def registro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')  # Redirige a la lista de clientes después del registro exitoso
    else:
        form = ClienteForm()  # Crea un formulario vacío si el método HTTP no es POST

    # Obtener las bicicletas disponibles para mostrar en el formulario
    bicicletas = Bicicleta.objects.all()

    context = {
        'form': form,
        'bicicletas': bicicletas,  # Pasar bicicletas al contexto
    }
    return render(request, 'bici/registro.html', context)

def modificar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('list')  # Redirige a la lista de clientes después de guardar
    else:
        form = ClienteForm(instance=cliente)

    context = {
        'form': form,
        'cliente': cliente,
    }
    return render(request, 'bici/modificar_cliente.html', context)

    
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        cliente.delete()
        return redirect('list')  # Redirige a la lista de clientes después de eliminar

    return render(request, 'bici/eliminar_cliente.html', {'cliente': cliente})

