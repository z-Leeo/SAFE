from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class regCapacitacion(models.Model):
    METODOLOGIA_CHOICES = [
        ('Presentaciones', 'Presentaciones'),
        ('Demostraciones', 'Demostraciones'),
        ('Ejercicios', 'Ejercicios Practicos'),
        ('Preguntas', 'Preguntas'),
    ]

    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    email = models.CharField(max_length=100 )
    nombre_curso = models.CharField(max_length=100)
    fecha_curso = models.DateField()
    genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    ubicacion_curso = models.CharField(max_length=100) 
    encargado_curso = models.CharField(max_length=100)
    metodologia_ensenanza = models.CharField(max_length=100, choices=METODOLOGIA_CHOICES, default='Presentaciones')
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()

    def __str__(self):
        return self.nombre_curso
    

    
class regMedico(models.Model):
    SERVICIO_CHOICES = [
        ('Cardiologo', 'Cardiologo'),
        ('Odontologia', 'Odontologia'),
        ('Medicina General', 'Medicina General'),
        ('Traumatologia', 'Traumatologia'),
        ('Psicologia','Psicologia'),
        ('Dermatologia','Dermatologia')
    ]

    id = models.AutoField(primary_key=True)
    nombre_completoM = models.CharField(max_length=100)
    rutM = models.CharField(max_length=100 )
    nombre_medicoM = models.CharField(max_length=100)
    fecha_atencionM = models.DateField()
    genero1 = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    previsionM = models.CharField(max_length=100) 
    ocupacionM = models.CharField(max_length=100)
    servicio_atencionM = models.CharField(max_length=100, choices=SERVICIO_CHOICES, default='Cardiologo')
    historialM = models.CharField(max_length=80)
    alergiaM = models.CharField(max_length=50)
    fecha_proxM = models.DateField()

    def __str__(self):
        return self.rutM
    

class regExamen(models.Model):
    SERVICIO_CHOICES = [
        ('Cardiologo', 'Cardiologo'),
        ('Odontologia', 'Odontologia'),
        ('Medicina General', 'Medicina General'),
        ('Traumatologia', 'Traumatologia'),
        ('Psicologia','Psicologia'),
        ('Dermatologia','Dermatologia')
    ]

    id = models.AutoField(primary_key=True)
    nombre_completoE = models.CharField(max_length=100, null=False ,default='')
    rutE = models.CharField(max_length=100, null=False )
    nombre_medicoE = models.CharField(max_length=100)
    fecha_examenE = models.DateField()
    generoE = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    resultadoE = models.CharField(max_length=100) 
    observacionE = models.CharField(max_length=100)
    servicio_atencionE = models.CharField(max_length=100, choices=SERVICIO_CHOICES, default='Cardiologo')
    historialE = models.CharField(max_length=80)
    tratamientoE = models.CharField(max_length=50)
    fecha_proxE = models.DateField()

    def __str__(self):
        return self.rutE
    


class regTerreno(models.Model):
    SERVICIO_CHOICES = [
        ('Subterraneo', 'Subterraneo'),
        ('Superficie', 'Superficie'),
        ('Cantera', 'Cantera'),
        ('Montaña', 'Montaña'),
        
    ]

    id = models.AutoField(primary_key=True)
    nombre_terreno = models.CharField(max_length=100)
    ubicacion_terreno = models.CharField(max_length=100 )
    topografia = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    riesgo1 = models.CharField(max_length=10, choices=[('Si', 'Si'), ('No', 'No')])
    clima = models.CharField(max_length=100) 
    obsevacionT = models.CharField(max_length=100)
    tipo_terreno = models.CharField(max_length=100, choices=SERVICIO_CHOICES, default='Subterraneo')
    deteccionQuimico = models.CharField(max_length=80)
    materialUt = models.CharField(max_length=50)
    salidas = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_terreno
    
class Contacto (models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    numero = models.IntegerField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre