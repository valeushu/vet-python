from apps.veterinaria.views import cliente_views
from django.urls import path


urlpatterns = [
    # ex: /polls/
    # path("", cliente_views.clientes, name="index"),

    path("lista", cliente_views.lista_clientes, name="lista_clientes"),
    path("signup/", cliente_views.signup, name="signup"),
    path("", cliente_views.home, name="home"),
    path("prueba", cliente_views.prueba, name="cliente_views"),
    path('cliente/editar/<int:id>',
         cliente_views.cliente_editar, name='cliente_editar'),
]
