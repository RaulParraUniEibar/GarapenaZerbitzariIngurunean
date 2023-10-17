from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Casas
from .models import Personas
from .models import Alquiler
# Create your views here.
def index (request):
    casas = Casas.objects.all
    personas = Personas.objects.all
    alquiler = Alquiler.objects.all
    return render(request, 'index.html', {'casas':casas, 'personas':personas,'alquiler':alquiler,})

def add(request): 
    casas = Casas.objects.all
    personas = Personas.objects.all
    return render(request,'add.html', {'casas':casas, 'personas':personas})

def addcasa(request): 
    nombre = request.POST["nombre"]
    ciudad = request.POST["ciudad"]
    numerodepersonas = request.POST["numerodepersonas"]
    casanueva = Casas(nombre=nombre, ciudad=ciudad,numerodepersonas=numerodepersonas)
    casanueva.save()

    return HttpResponseRedirect(reverse(index))

def addpersona(request): 
    nombre = request.POST["nombre"]
    email = request.POST["email"]
    dni = request.POST["dni"]
    personanueva = Personas(nombre=nombre, email=email,dni=dni)
    personanueva.save()

    return HttpResponseRedirect(reverse(index))


def addalquiler(request):
    perid = request.POST["nombreper"]
    casid = request.POST["nombrecas"]
    dia = request.POST["dia"]

    cas = Casas.objects.get(id = casid)
    per = Personas.objects.get(id = perid)

    alquilernuevo = Alquiler(dia=dia, personaalquiler= per, casaalquiler=cas)
    alquilernuevo.save()

    return HttpResponseRedirect(reverse(index))

def deletepersona(request, id):
    personaeliminar = Personas.objects.get(id = id)

    Personas.delete(personaeliminar)

    return HttpResponseRedirect(reverse(index))

def deletecasa(request, id):
    casaeliminar = Casas.objects.get(id = id)

    Casas.delete(casaeliminar)

    return HttpResponseRedirect(reverse(index))

def deletealquiler(request, id):
    alquilereliminar = Alquiler.objects.get(id = id) #pasar el equipo
    Personas.delete(alquilereliminar) #ezabatu

    return HttpResponseRedirect(reverse(index))

def updatepersona(request, id):
    personaUpdate = Personas.objects.get(id = id)
    return render(request,'update.html', {'per':personaUpdate})

def editarpersona(request, id):

    personaeditar = Personas.objects.get(id = id) #pasar el id del equipo

    nombre = request.POST["nombre"]
    email = request.POST["email"]
    dni = request.POST["dni"]

    personaeditar.nombre = nombre
    personaeditar.email = email
    personaeditar.dni = dni
    personaeditar.save()
       
    return HttpResponseRedirect(reverse(index))

def updatecasa(request, id):
    casaUpdate = Casas.objects.get(id = id)
    return render(request,'updatec.html', {'cas':casaUpdate})

def editarcasa(request, id):

    casaeditar = Casas.objects.get(id = id) #pasar el id del equipo

    nombre = request.POST["nombre"]
    ciudad = request.POST["ciudad"]
    numerodepersonas = request.POST["numerodepersonas"]

    casaeditar.nombre = nombre
    casaeditar.ciudad = ciudad
    casaeditar.numerodepersonas = numerodepersonas
    casaeditar.save()
       
    return HttpResponseRedirect(reverse(index))