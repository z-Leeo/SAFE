from django.contrib import admin
from .models import  regCapacitacion, regMedico, regExamen, regTerreno, Contacto

# Register your models here.


admin.site.register(regCapacitacion)
admin.site.register(regMedico)
admin.site.register(regExamen)
admin.site.register(regTerreno)
admin.site.register(Contacto)


