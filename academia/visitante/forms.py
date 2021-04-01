from django import forms
from .models import alcance,recomendacion,capitulo

class AlcanceForm(forms.ModelForm):
	class Meta:
		model = alcance
		fields = ['descripcion']
		widgets = {'descripcion': forms.TextInput(attrs={'class':'form-control'})}
		labels = {'descripcion': 'Descripcion del alcance'}

LISTA_NIVELES = (
				('Basico','Basico'),
				('Intermedio','Intermedio'),
				('Medio','Medio'),
				('Suficiente','Suficiente'),
				('Avanzado','Avanzado'),
			)
class RecomendacionForm(forms.ModelForm):
	class Meta:
		model = recomendacion
		fields = ['materia','nivel']
		widgets = {'materia': forms.TextInput(attrs={'class':'form-control'}),
				'nivel': forms.RadioSelect(choices=LISTA_NIVELES)
					}
		labels = {'materia': 'Materia recomendada'}
		
class CapituloForm(forms.ModelForm):
	class Meta:
		model = capitulo
		fields = ['nombre','descripcion']
		widgets = {'nombre': forms.TextInput(attrs={'class':'form-control'}),
				'descripcion': forms.Textarea(attrs={'class':'form-control'})
					}
		labels = {'nombre': 'Nombre del capitulo'}

from .models import tema

class TemaForm(forms.ModelForm):
	class Meta:
		model = tema
		fields = ['nombre','descripcion']
		widgets = {'nombre': forms.TextInput(attrs={'class':'form-control'}),
				'descripcion': forms.Textarea(attrs={'class':'form-control'})
					}
		labels = {'nombre': 'Nombre del tema'}

from .models import detalle

class DetalleForm(forms.ModelForm):
	class Meta:
		model = detalle
		fields = ['nombre','descripcion','dirurl', 'imagen','media','texto','referencia_imagen','referencia_media','referencia_texto']

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
			'dirurl': forms.Textarea(attrs={'class':'form-control'}),
			'imagen': forms.ClearableFileInput(attrs={'class':'form-control'}),
			'media': forms.ClearableFileInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'referencia_imagen': forms.TextInput(attrs={'class':'form-control'}),
			'referencia_media': forms.TextInput(attrs={'class':'form-control'}),
			'referencia_texto': forms.TextInput(attrs={'class':'form-control'}),
		}
		