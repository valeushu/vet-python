from django.urls import path


from apps.veterinaria.views import cliente_views

urlpatterns = [
    # ex: /polls/
    # path("", cliente_views.clientes, name="index"),

    path("", cliente_views.lista_clientes, name="lista_clientes"),
    path("prueba", cliente_views.prueba, name="cliente_views"),
    path('cliente/<int:id>/editar/',
         cliente_views.cliente_editar, name='cliente_editar'),
]
