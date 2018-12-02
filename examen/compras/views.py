from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Productos, Tienda
# Create your views here.

def index(request):
    return render(request, 'compras/inicio.html', {})

class ProductosList(ListView):
    model = Productos

class ProductosView(DetailView):
    model = Productos

class ProductosCreate(CreateView):
    model = Productos
    fields = ['nombre', 'costo_presupuesto', 'costo_real', 'tienda', 'notas']
    success_url = reverse_lazy('productos_list')

class ProductosUpdate(UpdateView):
    model = Productos
    fields = ['nombre', 'costo_presupuesto', 'costo_real', 'tienda', 'notas']
    success_url = reverse_lazy('productos_list')

class ProductosDelete(DeleteView):
    model = Productos
    success_url = reverse_lazy('productos_list')

class TiendaList(ListView):
    model = Tienda

class TiendaView(DetailView):
    model = Tienda

class TiendaCreate(CreateView):
    moodel = Tienda
    fields = ['nombre', 'sucursal', 'direccion', 'ciudad', 'region']
    success_url = reverse_lazy('tienda_list')

class TiendaUpdate(UpdateView):
    model = Tienda
    fields = ['nombre', 'sucursal', 'direccion', 'ciudad', 'region']
    success_url = reverse_lazy('tienda_list')

class TiendaDelete(DeleteView):
    model = Tienda
    success_url = reverse_lazy('tienda_list')