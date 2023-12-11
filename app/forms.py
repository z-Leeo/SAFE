from django import forms
from .models import regCapacitacion, regMedico, regExamen, regTerreno

    


class FormulariosForm(forms.ModelForm):
    class Meta:
        model = regCapacitacion
        fields = '__all__'

class MedicoForm(forms.ModelForm):
    class Meta:
        model = regMedico
        fields = '__all__'

class ExamenForm(forms.ModelForm):
    class Meta:
        model = regExamen
        fields = '__all__'

class TerrenoForm(forms.ModelForm):
    class Meta:
        model = regTerreno
        fields = '__all__'