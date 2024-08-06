from django import forms
from .models import Tarea, Subtarea

# class TareaForm(forms.ModelForm):
#     class Meta:
#         model = tarea
#         fields = 'description','eliminada'  # O especifica los campos que deseas mostrar en el formulario

# class SubTareaForm(forms.ModelForm):
#     class Meta:
#         model = subtarea
#         fields = 'description','eliminada'  # O especifica los campos que deseas mostrar en el formulario

# class TareaFormForm(forms.Form):
#     tarea_description = forms.CharField(max_length=100)
#     tarea_eliminada = forms.BooleanField()
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['description', 'eliminada']
            
# class SubTareaFormForm(forms.Form):
#     sub_tarea_description = forms.CharField(max_length=100)
#     sub_tarea_eliminada = forms.BooleanField()
