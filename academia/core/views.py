from django.shortcuts import render
from django.http import HttpResponse

from .models import curso

# Create your views here.
def homeView(request):
    lista_ultimos = curso.objects.filter(completo=True).order_by('created').reverse()[0:5]
    mejores_gratuitos = curso.objects.filter(precio=0, completo=True).order_by('alumnos').reverse()[0:5]
    return render(request, "home.html", {'lista':lista_ultimos,'mejores_gratuitos':mejores_gratuitos})

from .forms import CursoForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def NuevoCursoView(request):
	mensaje = "Esta es la etepa previa al Submit"
	titulo_template = "Registro de un nuevo curso"
	form = CursoForm(request.POST)
	if request.method == 'POST':
		mensaje = "Todo fue exitoso"
		form = CursoForm(request.POST,request.FILES)
		if form.is_valid():
			Curso = form.save(commit=False)
			Curso.alumnos = 0
			Curso.calificacion = 0
			Curso.profesor = request.user.username
			Curso.save()
			User = request.user
			if User.first_name == 'a':
				User.first_name = 'b'
			else:
				User.first_name = 'p'
			User.save()
			return HttpResponseRedirect(reverse('core:home'))
		else:
			mensaje="Ha ocurrido un error"
	return render(request,'curso.html',{'form':form,'mensaje':mensaje,'titulo_template':titulo_template})    

from django.contrib.auth.models import AnonymousUser

def DetalleCursoView(request, pk):
	Curso = curso.objects.get(id=pk)
	reviews = 56
	estado  = 'n'
	if not request.user == AnonymousUser():
		estado = 's'
		# Perfil = perfil.objects.get(user=request.user)
		# if Perfil.vistante == True:
		# 	estado = 's'
		# elif Perfil.alumnno == True:
		# 	estado = 's'
		# else:
		# 	estado = 's'
	return render(request,'detalle_curso.html',{'curso':Curso,'reviews':reviews,'estado': estado})

def ListaCursosView(request):
	criterio = request.GET['criterio']
	print('criterio')
	lista= None
	if criterio == '*':
		lista = curso.objects.all()
	elif criterio != '':
		lista=curso.objects.filter(titulo__icontains = criterio) | curso.objects.filter(descripcion__icontains = criterio)
	return render(request,'lista_cursos.html',{'lista':lista})

def EnPreparacionView(request):
	lista = None
	lista = curso.objects.filter(completo=False,profesor=request.user)
	return render (request,'en_preparacion.html',{'lista':lista})

def EditarCursoView(request,pk):
	mensaje = ''
	Curso = curso.objects.get(id=pk)
	titulo_template = "Edicion del curso"
	titulo = Curso.titulo
	form = CursoForm(instance=Curso)
	if request.method == 'POST':
		form = CursoForm(request.POST,request.FILES,instance=Curso)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('core:en_preparacion'))
		else:
			mensaje='Ha ocurrido un error'
	return render(request,'curso.html',{'form':form,'mensaje':mensaje,'titulo_template':titulo_template,'titulo':titulo})	

def BorrarCursoView(request,pk):
	Curso = curso.objects.get(id=pk)
	Curso.delete()
	return HttpResponseRedirect(reverse('core:en_preparacion'))	

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import disciplina
from .forms import DisciplinaForm

class DisciplinaListView(ListView):
	model = disciplina

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		lista = disciplina.objects.all()
		context['lista'] = lista
		return context

class DisciplinaCreateView(CreateView):
	model = disciplina
	form_class = DisciplinaForm
	success_url = reverse_lazy('core:lista_disciplinas')

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo_template'] = "Registro de una nueva disciplina"			
		return context

class DisciplinaUpdateView(UpdateView):
	model = disciplina
	form_class = DisciplinaForm
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('core:lista_disciplinas')

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		Disciplina = self.object
		context['titulo_template'] = "Edicion de: "
		context['titulo'] = Disciplina.nombre
		return context			

class DisciplinaDeleteView(DeleteView):
	model = disciplina
	success_url = reverse_lazy('core:lista_disciplinas')

from .models import inscripcion
from registration.models import perfil

def InscripcionView(request,**kwargs):
	user = request.user
	if kwargs['curso'] >0:
		Curso = curso.objects.get(id=kwargs['curso'])
		# Buscar si ya esta inscrito
		lista = inscripcion.objects.filter(curso=Curso,alumno=user)
		if lista.count() == 0:
			Inscripcion = inscripcion()
			Inscripcion.alumno = user
			Inscripcion.curso = Curso
			Inscripcion.save()
			# Cambia el estado del usuario
			# Obtiene el perfil
			Perfil = perfil.objects.get(user=user)
			Perfil.alumno = True
			Perfil.visitante = False
			Perfil.save()
			Curso.alumnos += 1
			Curso.save()
			if user.first_name == 'p':
				user.first_name = 'b'
			else:
				user.first_name = 'a'
			user.save()
	lista = inscripcion.objects.filter(alumno=user)
	return render(request,'core/inscripcion_lista.html',{'lista_inscripcion':lista})

from visitante.models import capitulo,tema,detalle


def EstudioView(request, **kwargs):
	Curso = curso.objects.get(id=kwargs['curso'])
	capitulos=[]
	temas=[]
	detalles=[]

	for cap in capitulo.objects.filter(curso=Curso):
		capitulos.append(cap)
		for tem in tema.objects.filter(capitulo=cap):
			temas.append(tem)
			for det in detalle.objects.filter(tema=tem):
				detalles.append(det)

	# Estudio
	contenido = []
	for cap in capitulo.objects.filter(curso=Curso):
		contenido.append([cap,'capitulo'])
		for tem in tema.objects.filter(capitulo=cap):
			contenido.append([tem,'tema'])
			for det in detalle.objects.filter(tema=tem):
				contenido.append([det,'detalle'])

	return render(request,'core/estudio.html',{'capitulos':capitulos,'temas':temas,'detalles':detalles,'curso':Curso,'contenido':contenido})

def ConstruidoView(request):
	User = request.user
	lista = curso.objects.filter(profesor=User,completo=True)
	return render(request,'core/construido.html',{'lista':lista})	