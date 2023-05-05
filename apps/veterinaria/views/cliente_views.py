from django.http import HttpResponse
from django.shortcuts import render
from ..models.Clientes import Cliente
from ..forms.ClienteForm import ClienteForm

from django.shortcuts import render, get_object_or_404, redirect


def lista_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'cliente/lista_clientes.html', context)


def cliente_editar(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/editar.html', {'form': form})


def prueba(request):
    return HttpResponse('bienvenida')
