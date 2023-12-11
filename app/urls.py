from django.urls import path, re_path   
from django.contrib.auth import views as auth_views
from .views import home, servicio, registro, consulta, informe,registroPC,\
registroET,registroAM,registroAE,consultaVM,consultaInfoM,consultaIC,salir,\
buscar,consulta_registro_vm, modificar_formulario,modificar_formulario1,\
modificar_formulario2, modificar_formulario3,eliminar_formulario, eliminar_formulario1,\
eliminar_formulario2, eliminar_formulario3,NotFoundView


urlpatterns = [
    path('', home, name="home"),
    path('servicio/', servicio, name="servicio"),
    path('registro/', registro, name="registro"),
    path('consulta/', consulta, name="consulta"),
    path('informe/', informe, name="informe"),
    path('registroPC/', registroPC, name="registroPC"),
    path('registroET/', registroET, name="registroET"),
    path('registroAM/', registroAM, name="registroAM"),
    path('registroAE/', registroAE, name="registroAE"),
    path('consultaVM/', consultaVM, name="consultaVM"),
    path('consultaInfoM/', consultaInfoM, name="consultaInfoM"),
    path('consultaIC/', consultaIC, name="consultaIC"),
    path('salir/', salir, name='salir'),
    path('buscar/', buscar, name='buscar'), # type: ignore
    path('consulta_vm/', consulta_registro_vm, name='consulta_registro_vm'),
    path('modificar_formulario/<id>/', modificar_formulario, name="modificar_formulario"),
    path('modificar_formulario1/<id>/', modificar_formulario1, name="modificar_formulario1"),
    path('modificar_formulario2/<id>/', modificar_formulario2, name="modificar_formulario2"),
    path('modificar_formulario3/<id>/', modificar_formulario3, name="modificar_formulario3"),
    path('eliminar_formulario/<id>/', eliminar_formulario, name = "eliminar_formulario"),
    path('eliminar_formulario1/<id>/', eliminar_formulario1, name = "eliminar_formulario1"),
    path('eliminar_formulario2/<id>/', eliminar_formulario2, name = "eliminar_formulario2"),
    path('eliminar_formulario3/<id>/', eliminar_formulario3, name = "eliminar_formulario3"),

]

urlpatterns += [
    re_path(r'^.*/$', NotFoundView.as_view(), name='not_found'),
]