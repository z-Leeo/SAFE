from django.shortcuts import get_object_or_404, render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render,redirect
from .models import *

from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.db.models import Q



from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

from django.views import View


class NotFoundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/404.html', status=404)

def home (request):
    return render(request, 'app/home.html')

@login_required
def servicio (request):
    return render(request, 'app/servicio.html')

def registro (request):
    return render(request, 'app/registro.html')

def consulta (request):
    return render(request, 'app/consulta.html')

def informe (request):
    return render(request, 'app/informe.html')


@permission_required('app.add_regcapacitacion')
def registroPC (request):
    return render(request, 'app/registroPC.html')


@permission_required('app.add_regterreno')
def registroET (request):
    return render(request, 'app/registroET.html')

@permission_required('app.add_regmedico')
def registroAM (request):
    return render(request, 'app/registroAM.html')

@permission_required('app.add_regmedico')
def registroAE (request):
    return render(request, 'app/registroAE.html')
@login_required
def consultaVM (request):
    return render(request, 'app/consultaVM.html')
@login_required
def consultaInfoM (request):
    return render(request, 'app/consultaInfoM.html')
@login_required
def consultaIC (request):
    return render(request, 'app/consultaIC.html')
    
def salir(request):
    logout(request)
    return render(request,'home.html')

from .forms import FormulariosForm, MedicoForm, ExamenForm, TerrenoForm


@permission_required('app.change_regcapacitacion')
def modificar_formulario(request, id):
    # Obtener la instancia del formulario a modificar
    formulario_instance = get_object_or_404(regCapacitacion, id=id)

    # Manejar el formulario con la instancia obtenida
    form = FormulariosForm(instance=formulario_instance)

    if request.method == 'POST':
        form = FormulariosForm(request.POST, instance=formulario_instance)
        if form.is_valid():
            # Guardar los cambios en la instancia del formulario
            form.save()
            return redirect('informe')

    context = {'form': form}

    return render(request, 'app/modificar.html', context)



@permission_required('app.change_regmedico')
def modificar_formulario1(request, id):
    # Obtener la instancia del formulario a modificar
    formulario_instance1 = get_object_or_404(regMedico, id=id)

    # Manejar el formulario con la instancia obtenida
    form1 = MedicoForm(instance=formulario_instance1)

    if request.method == 'POST':
        form1 = MedicoForm(request.POST, instance=formulario_instance1)
        if form1.is_valid():
            # Guardar los cambios en la instancia del formulario
            form1.save()
            return redirect('informe')

    context1 = {'form1': form1}

    return render(request, 'app/modificar1.html', context1)

@permission_required('app.change_regexamen')
def modificar_formulario2(request, id):
    # Obtener la instancia del formulario a modificar
    formulario_instance2 = get_object_or_404(regExamen, id=id)

    # Manejar el formulario con la instancia obtenida
    form2 = ExamenForm(instance=formulario_instance2)

    if request.method == 'POST':
        form2 = ExamenForm(request.POST, instance=formulario_instance2)
        if form2.is_valid():
            # Guardar los cambios en la instancia del formulario
            form2.save()
            return redirect('informe')

    context2 = {'form2': form2}

    return render(request, 'app/modificar2.html', context2)

@permission_required('app.change_regterreno')
def modificar_formulario3(request, id):
    # Obtener la instancia del formulario a modificar
    formulario_instance3 = get_object_or_404(regTerreno, id=id)

    # Manejar el formulario con la instancia obtenida
    form3 = TerrenoForm(instance=formulario_instance3)

    if request.method == 'POST':
        form3 = TerrenoForm(request.POST, instance=formulario_instance3)
        if form3.is_valid():
            # Guardar los cambios en la instancia del formulario
            form3.save()
            return redirect('informe')

    context3 = {'form3': form3}

    return render(request, 'app/modificar3.html', context3)


@permission_required('app.delete_regcapacitacion')
def eliminar_formulario(request, id):
    formulario_instance = get_object_or_404(regCapacitacion, id = id)
    formulario_instance.delete()
    return redirect(to = 'informe')

@permission_required('app.delete_regmedico')
def eliminar_formulario1(request, id):
    formulario_instance1 = get_object_or_404(regMedico, id = id)
    formulario_instance1.delete()
    return redirect(to = 'informe')


@permission_required('app.delete_regexamen')
def eliminar_formulario2(request, id):
    formulario_instance2 = get_object_or_404(regExamen, id = id)
    formulario_instance2.delete()
    return redirect(to = 'informe')


@permission_required('app.delete_regterreno')
def eliminar_formulario3(request, id):
    formulario_instance3 = get_object_or_404(regTerreno, id = id)
    formulario_instance3.delete()
    return redirect(to = 'informe')





from django.db.models import Q


@login_required
def buscar(request):
    termino = request.GET.get('buscar')

    # Filtra tus modelos según el término de búsqueda
    capacitaciones = regCapacitacion.objects.filter(
        Q(nombre_completo__icontains=termino) | 
        Q(email__icontains=termino) 
        # Agrega más campos según tus necesidades
    )

    atenciones = regMedico.objects.filter(
        Q(nombre_completoM__icontains=termino) |
        Q(rutM__icontains=termino) 
        # Agrega más campos según tus necesidades
    )

    examenes = regExamen.objects.filter(
        Q(nombre_completoE__icontains=termino) |
        Q(rutE__icontains=termino) 
        # Agrega más campos según tus necesidades
    )

    data = {
        'capacitaciones': capacitaciones,
        'atenciones': atenciones,
        'examenes' : examenes,
    }

    return render(request, "app/informe.html", data)

@permission_required('app.view_regmedico')
def consulta_registro_vm(request):
    registro_id = request.GET.get('registro_id')
    registro = regMedico.objects.filter(rutM=registro_id).first()
    registro = regMedico.objects.filter(nombre_completoM=registro_id).first()

    return render(request, 'app/consultaVM.html', {
        'registro': registro
    })

@permission_required('app.view_regexamen')
def consultaInfoM(request):
    registro_id = request.GET.get('registro_id')
    registro = regExamen.objects.filter(rutE=registro_id).first()
    registro = regExamen.objects.filter(nombre_completoE=registro_id).first()

    return render(request, 'app/consultaInfoM.html', {
        'registro': registro
    })

@permission_required('app.view_regcapacitacion')
def consultaIC(request):
    registro_id = request.GET.get('registro_id')
    registro = regCapacitacion.objects.filter(nombre_completo=registro_id).first()

    return render(request, 'app/consultaIC.html', {
        'registro': registro
    })

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_trabajador = 'trabajador' in request.POST
        is_ingtec = 'ingtec' in request.POST
        is_supervisor = 'supervisor' in request.POST

        if not any([is_trabajador, is_ingtec, is_supervisor]):
            # Puedes manejar el error de alguna manera, por ejemplo, mostrar un mensaje de error.
            return render(request, 'registration/registro.html', {'error_message': 'Selecciona al menos un grupo de usuario.'})

        # Crear el usuario
        user = User.objects.create_user(username=username, password=password)

        # Asignar el grupo correspondiente al usuario
        if is_trabajador:
            trabajador_group, _ = Group.objects.get_or_create(name='trabajador')
            user.groups.add(trabajador_group)
        if is_ingtec:
            ingtec_group, _ = Group.objects.get_or_create(name='ingtec')
            user.groups.add(ingtec_group)
        if is_supervisor:
            supervisor_group, _ = Group.objects.get_or_create(name='supervisor')
            user.groups.add(supervisor_group)

        # Redirigir a la página de inicio de sesión
        return redirect('login')  # Reemplaza 'nombre_de_la_url_de_login' con el nombre de la URL de tu vista de inicio de sesión.

    return render(request, 'registration/registro.html')


def salir(request):
    logout(request)
    return render(request,'app/home.html')

from django.contrib.auth.decorators import user_passes_test

# Función de prueba para verificar si el usuario pertenece al grupo "admin"
def user_belongs_to_admin_group(user):
    return user.groups.filter(name='admin').exists()

from django.http import HttpResponseBadRequest




def home (request):
    if request.method == 'POST':
        nombreContc = request.POST.get('nombre')
        correoContc = request.POST.get('email')
        numeroContc = request.POST.get('numero')
        asuntoContc = request.POST.get('asunto')
        mensajeContc = request.POST.get('mensaje')

        contactoHome = Contacto.objects.create(nombre = nombreContc
                                                ,email = correoContc
                                                ,numero = numeroContc
                                                ,asunto = asuntoContc
                                                ,mensaje = mensajeContc)
        contactoHome.save()
        return redirect('home')
    return render (request , 'app/home.html')


from django.shortcuts import render, redirect
from .models import regCapacitacion

@permission_required('app.add_regcapacitacion')
def registroPC(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_completo')
        correoo = request.POST.get('email')
        nombreC = request.POST.get('nombre_curso')
        fecha_cur = request.POST.get('fecha_curso')
        gender = request.POST.get('genero')
        ubicacion_cur = request.POST.get('ubicacion_curso')
        encargado_cur = request.POST.get('encargado_curso')
        metodologia_ens = request.POST.get('metodologia_ensenanza')
        city = request.POST.get('ciudad')
        reg = request.POST.get('region')
        codigo_post = request.POST.get('codigo_postal')
  

        #guardar en BD
        capacitacion = regCapacitacion.objects.create(nombre_completo=nombre
                                                    ,email=correoo
                                                    ,nombre_curso=nombreC
                                                    ,fecha_curso=fecha_cur
                                                    ,genero=gender
                                                    ,ubicacion_curso=ubicacion_cur
                                                    ,encargado_curso=encargado_cur
                                                    ,metodologia_ensenanza=metodologia_ens
                                                    ,ciudad=city
                                                    ,region=reg
                                                    ,codigo_postal=codigo_post
                                 )
        capacitacion.save()
        return redirect('informe')
    return render(request, 'app/registroPC.html')

@permission_required('app.add_regterreno')
def registroET(request):
    if request.method == 'POST':
        nombreter = request.POST.get('nombre_terreno')
        ubicT = request.POST.get('ubicacion_terreno')
        topo = request.POST.get('topografia')
        fecT = request.POST.get('fecha_registro')
        risk = request.POST.get('riesgo1')
        tiempo = request.POST.get('clima')
        observT = request.POST.get('obsevacionT')
        tipoTer = request.POST.get('tipo_terreno')
        quimico = request.POST.get('deteccionQuimico')
        material = request.POST.get('materialUt')
        salida = request.POST.get('salidas')
  

        #guardar en BD
        terreno = regTerreno.objects.create(nombre_terreno=nombreter
                                                    ,ubicacion_terreno=ubicT
                                                    ,topografia=topo
                                                    ,fecha_registro=fecT
                                                    ,riesgo1=risk
                                                    ,clima=tiempo
                                                    ,obsevacionT=observT
                                                    ,tipo_terreno=tipoTer
                                                    ,deteccionQuimico=quimico
                                                    ,materialUt=material
                                                    ,salidas=salida
                                 )
        terreno.save()
        return redirect('informe')
    return render(request, 'app/registroET.html')

@permission_required('app.add_regmedico')
def registroAM(request):
    if request.method == 'POST':
        nombrePac = request.POST.get('nombre_completoM')
        rutPac = request.POST.get('rutM')
        nombreMed = request.POST.get('nombre_medicoM')
        fecha_Med = request.POST.get('fecha_atencionM')
        gender1 = request.POST.get('genero1')
        prev = request.POST.get('previsionM')
        ocup = request.POST.get('ocupacionM')
        serv_at = request.POST.get('servicio_atencionM')
        hist = request.POST.get('historialM')
        alerg = request.POST.get('alergiaM')
        fecha_prox = request.POST.get('fecha_proxM')
  

        #guardar en BD
        atencion = regMedico.objects.create(nombre_completoM=nombrePac
                                                    ,rutM=rutPac
                                                    ,nombre_medicoM=nombreMed
                                                    ,fecha_atencionM=fecha_Med
                                                    ,genero1=gender1
                                                    ,previsionM=prev
                                                    ,ocupacionM=ocup
                                                    ,servicio_atencionM=serv_at
                                                    ,historialM=hist
                                                    ,alergiaM=alerg
                                                    ,fecha_proxM=fecha_prox
                                 )
        atencion.save()
        return redirect('informe')
    return render(request, 'app/registroAM.html')




@permission_required('app.add_regexamen')
def registroAE(request):
    if request.method == 'POST':
        nombrePac1 = request.POST.get('nombre_completoE')
        rutPac1 = request.POST.get('rutE')
        nombreMed1 = request.POST.get('nombre_medicoE')
        fecha_Med1 = request.POST.get('fecha_examenE')
        gender2 = request.POST.get('generoE')
        result = request.POST.get('resultadoE')
        observ = request.POST.get('observacionE')
        serv_atE = request.POST.get('servicio_atencionE')
        histE = request.POST.get('historialE')
        trat = request.POST.get('tratamientoE')
        fecha_proxE = request.POST.get('fecha_proxE')
  

        #guardar en BD
        examen = regExamen.objects.create(nombre_completoE=nombrePac1
                                                    ,rutE=rutPac1
                                                    ,nombre_medicoE=nombreMed1
                                                    ,fecha_examenE=fecha_Med1
                                                    ,generoE=gender2
                                                    ,resultadoE=result
                                                    ,observacionE=observ
                                                    ,servicio_atencionE=serv_atE
                                                    ,historialE=histE
                                                    ,tratamientoE=trat
                                                    ,fecha_proxE=fecha_proxE
                                 )
        examen.save()
        return redirect('informe')
    return render(request, 'app/registroAE.html')


@login_required
def informe(request):
    capacitaciones = regCapacitacion.objects.all()
    atenciones = regMedico.objects.all()
    examenes = regExamen.objects.all()
    terrenos = regTerreno.objects.all()
    data = {
        'capacitaciones': capacitaciones,
        'atenciones': atenciones,
        'examenes' : examenes,
        'terrenos' : terrenos,
    }
    return render(request, "app/informe.html", data)

def user_belongs_to_admin_group(user):
    return user.groups.filter(name='admin').exists()

# Vista protegida solo para miembros del grupo "admin"
@user_passes_test(user_belongs_to_admin_group, login_url='login')
def vista_admin_mensajes(request):
    informes = regCapacitacion.objects.all()
    return render(request, 'app/informe.html', {'informes': informes})


