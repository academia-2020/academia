from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegistroConMail

from .models import perfil

# Create your views here.
def RegistroView(request):
	mensaje = "Esta es la etepa previa al Submit"
	form = RegistroConMail(request.POST)
	if request.method == 'POST':
		mensaje = "Todo fue exitoso"
		form = RegistroConMail(request.POST,request.FILES)
		if form.is_valid():
			usuario = form.save(commit=False)
			usuario.first_name = 'v'
			usuario.save()
			nuevo_perfil = perfil()
			nuevo_perfil.user = usuario
			nuevo_perfil.nombre=''
			nuevo_perfil.recibemails=True
			nuevo_perfil.visitante = True
			nuevo_perfil.save()
			return HttpResponseRedirect(reverse('core:home'))
		else:
			mensaje="Ha ocurrido un error"
	return render(request,'registration/registro.html',{'form':form,'mensaje':mensaje})    

from .forms import PerfilForm

def PerfilView(request):
	mensaje = "Esta es la etepa previa al Submit"
	user = request.user
	form = PerfilForm(request.POST)
	if request.method == 'POST':
		mensaje = "Todo fue exitoso"
		form = PerfilForm(request.POST,request.FILES)
		if form.is_valid():
			Perfil = form.save(commit=False)
			Perfil.user = user
			Perfil.save()
			return HttpResponseRedirect(reverse('core:home'))
		else:
			mensaje="Ha ocurrido un error"
	return render(request,'registration/registro.html',{'form':form,'mensaje':mensaje})    	

from django.shortcuts import redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def CambioPasswordView(request):
	form = PasswordChangeForm(request.user)
	mensaje = ''
	if request.method == 'POST':
		form=PasswordChangeForm(request.user,request.POST)
		if form.isvalid():
			user=form.save()
			update_session_auth_hash(request.user)
			return redirect('core:home')
		else:
			mensaje='Por favor vuelva a intentarlo'
	return render(request,'registration/cambio_password.html',{'form':form,'mensaje':mensaje})

def PerfilUpdateView(request):
	mensaje = ''
	user = request.user
	Perfil = perfil.objects.get(user=user)
	form = PerfilForm(instance=Perfil)
	if request.method == 'POST':
		form = PerfilForm(request.POST,request.FILES,instance=Perfil)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('core:home'))
		else:
			mensaje='Ha ocurrido un error'
	return render(request,'registration/perfil.html',{'form':form,'mensaje':mensaje})