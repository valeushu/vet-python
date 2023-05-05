from django import forms
from ..models.Clientes import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('dni', 'nombre', 'apellido',
                  'ciudad', 'direccion', 'telefono')
