from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, login, servicio, registro, consulta, informe,registroPC,registroET,registroAM,registroAE,consultaVM,consultaInfoM,consultaIC,salir, buscar,consulta_registro_vm

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
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
]
