from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index, name='index'),
    path('autor/',views.abrirAutor, name='Autor'),
    path('Cargar-configuraciones/',views.cargaMasiva,name='cargaConfig'),
    path('Cargar-consumos/',views.cargaMasiva2,name='cargaConsu'),
    path('Consulta-recursos/',views.verRecursos,name='consultaRecursos'),
    path('Consulta-Clientes/',views.verClientes,name='consultaClientes'),
    path('Consulta-Categorias/',views.verCategorias,name='consultaCategorias'),
    path('Crear-recurso/',views.addRecurso,name='crearRecurso'),
    path('Crear-categoria/',views.addCategoria,name='crearCategoria'),
    path('Crear-configuracion/',views.addConfiguracion,name='crearConfiguracion'),
    path('Crear-cliente/',views.addCliente,name='crearCliente'),
    path('Crear-instancia/',views.addInstancia,name='crearInstancia')
]