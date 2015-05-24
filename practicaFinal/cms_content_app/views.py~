from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseNotFound,\
HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseRedirect
from models import Contenidos
from models import Usuario
from models import FechaActualizacion
from models import Membership
from django.views.decorators.csrf import csrf_exempt
from barrapunto import getBarrapunto
from django.template.loader import get_template
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import Context,RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import datetime, date, time, timedelta
import calendar

# Create your views here.

Actividades=""

def FormFilter():
    formulario = '<form action="/actualizar" method="GET">'+\
                 '<input type="submit" value="Actualizar actividades">'+\
                 '</form>'+\
                 '<form action="" method="POST" accept-charset="UTF-8">' +\
                 'Titulo: <input type="text" name="titulo">' +\
                 'Precio: <input type="text" name="precio">' +\
                 'Fecha: <input type="text" name="fecha">' +\
                 '<input type="submit" value="Enviar"></form>'+\
                 '<br/>'
    return formulario

@csrf_exempt
def Todas(request):
    if request.user.is_authenticated():
        (mensaje, admin, logger, request.user.username) = autenticacionUsuario(request)
        nombreUsuario = request.user.username
        usuario = Usuario.objects.filter(nombre= nombreUsuario)
        salida = ""
        nameUser = True
        for fila in usuario:
            if fila.nombre == nombreUsuario:
                nameUser = False
        if nameUser:
            principal = "Pagina de " + request.user.username
            comentarioPrincipal = "Introduzca descripcion..."
            name = Usuario(titulo= principal, nombre= request.user.username, comentario= comentarioPrincipal)
            name.save()

    salida= ""
    formulario = FormFilter()
    num = 0
    f = FechaActualizacion.objects.all()
    for fila in f:
        UltimaFecha = str(fila.fecha)
    fechaActualizada = "Fecha de ultima actualizacion: " + UltimaFecha + "<br/>"
    if request.method == "GET":
        lista = Contenidos.objects.all()
        (mensaje, admin, logger, usuario) = autenticacionUsuario(request)
        for fila in lista:
            salida += "<br/>" + "<br/>"
            salida += "Titulo: " + fila.titulo + "<br/>"
            salida += "Tipo: " + fila.tipo + "<br/>"
            salida += "Precio: " + fila.precio + "<br/>"
            salida += "Fecha: " + str(fila.fecha) + "<br/>"
            salida += "Hora: " + str(fila.hora) + "<br/>"
            salida += "Fecha Fin: " + str(fila.fechaFin) + "<br/>"
            salida += "Evento Largo: " + str(fila.eventoLargo) + "<br/>"
            salida += "<a href="+ fila.informacion + ">" + '+ info' + '</a>' + "<br/>"
            if request.user.is_authenticated():
                salida += '<form action="/guardar/' + str(fila.id) +'" method="GET">'+\
                          '<input type="submit" value="Guardar Actividad">'+\
                          '</form>'
            salida += "<br/>"
            num = num + 1
    
    if request.method == "POST":
        filtrarTitulo = request.POST.get("titulo")
        if filtrarTitulo:
            lista = Contenidos.objects.filter(titulo=filtrarTitulo)
        filtrarPrecio = request.POST.get("precio")
        if filtrarPrecio:
            lista = Contenidos.objects.filter(precio=filtrarPrecio)
        filtrarFecha = request.POST.get("fecha")
        if filtrarFecha:
            lista = Contenidos.objects.filter(fecha=filtrarFecha)

        (mensaje, admin, logger, usuario) = autenticacionUsuario(request)
        for fila in lista:
            salida += "<br/>" + "<br/>"
            salida += "Titulo: " + fila.titulo + "<br/>"
            salida += "Tipo: " + fila.tipo + "<br/>"
            salida += "Precio: " + fila.precio + "<br/>"
            salida += "Fecha: " + str(fila.fecha) + "<br/>"
            salida += "Hora: " + str(fila.hora) + "<br/>"
            salida += "Fecha Fin: " + str(fila.fechaFin) + "<br/>"
            salida += "Evento Largo: " + str(fila.eventoLargo) + "<br/>"
            salida += "<a href="+ fila.informacion + ">" + '+ info' + '</a>' + "<br/>"
            if request.user.is_authenticated():
                salida += '<form action="/guardar/' + str(fila.id) +'" method="GET">'+\
                          '<input type="submit" value="Guardar Actividad">'+\
                          '</form>'
            salida += "<br/>"
            num = num + 1
    numAct = "Numero Actividades: " + str(num) + "<br/>"

    return render_to_response ('todas.html', {'Espacio': "<br/>",'mensaje':mensaje, 'admin': admin, 'logger': logger,'form': formulario,'fecha': fechaActualizada,'num':numAct,'lista': salida}, context_instance=RequestContext(request))

def Actualizar(request):
    global Actividades
    Actividades = getBarrapunto()
    lista = Contenidos.objects.all()

    hoy = date.today()
    fechaHoy = str(hoy)
    Fecha = FechaActualizacion(fecha= fechaHoy)
    Fecha.save()

    todas = "/todas"
    return HttpResponseRedirect(todas)    

def PaginaPrincipal(request):
    cont= Contenidos.objects.order_by("fecha")
    hoy = date.today()
    formulario = ""
    (mensaje, admin, logger, usuario) = autenticacionUsuario(request)
    salida = ""
    paginas = ""
    listaPag = "<br/>"+ "<br/>" + "Paginas de usuarios disponibles" + "<br/>"
    numActividad = 0
    n = 0
    lista = [cont[1],cont[2],cont[3],cont[4],cont[5],
             cont[6],cont[7],cont[8],cont[9],cont[10]]
    for fila in lista:
        salida += "<br/>" + "<br/>"
        salida += "Actividad" + "<br/>"
        salida += "Titulo: " + fila.titulo + "<br/>"
        salida += "Tipo: " + fila.tipo + "<br/>"
        salida += "Precio: " + fila.precio + "<br/>"
        salida += "Fecha: " + str(fila.fecha) + "<br/>"
        salida += "Hora: " + str(fila.hora) + "<br/>"
        salida += "Fecha Fin: " + str(fila.fechaFin) + "<br/>"
        salida += "Evento Largo: " + str(fila.eventoLargo) + "<br/>"
        salida += "<a href="+ fila.informacion + ">" + '+ info' + '</a>' + "<br/>"
    usuarios = Usuario.objects.all()
    for user in usuarios:
       paginas += "<a href="+ '/' + user.nombre + ">" + user.titulo + '</a>'
       paginas += "  ===========>  "
       paginas += "<a href="+ '/' + user.nombre + '/rss' + ">" + 'RSS del usuario' + '</a>' + "<br/>"  

    return render_to_response('principal.html',{'lista': salida,'enlaces': paginas,'listado': listaPag, 'mensaje':mensaje, 'admin': admin, 'logger': logger}, context_instance=RequestContext(request))

@csrf_exempt
def user(request):
    if request.user.is_authenticated():
        (mensaje, admin, logger, request.user.username) = autenticacionUsuario(request)
        nombreUsuario = request.user.username
        usuario = Usuario.objects.filter(nombre= nombreUsuario)
        salida = ""
        nameUser = True
        Incluido = False
        num = 0
        for fila in usuario:
            if fila.nombre == nombreUsuario:
                nameUser = False
        if nameUser:
            principal = "Pagina de " + request.user.username
            comentarioPrincipal = "Introduzca descripcion..."
            name = Usuario(titulo= principal, nombre= request.user.username, comentario= comentarioPrincipal)
            name.save()
 
        userName = Usuario.objects.get(nombre=nombreUsuario)
        listaActividades = userName.actividades.all()
        for fila in listaActividades:
            salida += "<br/>" + "<br/>"
            salida += "Actividad" + "<br/>"
            salida += "Titulo: " + fila.titulo + "<br/>"
            salida += "Tipo: " + fila.tipo + "<br/>"
            salida += "Precio: " + fila.precio + "<br/>"
            salida += "Fecha: " + str(fila.fecha) + "<br/>"
            salida += "Hora: " + str(fila.hora) + "<br/>"
            salida += "Fecha Fin: " + str(fila.fechaFin) + "<br/>"
            salida += "Evento Largo: " + str(fila.eventoLargo) + "<br/>"
            salida += "<a href="+ fila.informacion + ">" + '+ info' + '</a>' + "<br/>"
            member = Membership.objects.get(contenido=fila, usuario=userName)
            fechaAct = member.fechaEleccion
            salida += "elegida en " + str(fechaAct) + "<br/>"
            salida += "<br/>"
            num = num + 1

        salida +='<form action="" method="POST" accept-charset="UTF-8">' +\
                 'Titulo: <input type="text" name="titulo">' +\
                 'Descripcion: <input type="text" name="descripcion">' +\
                 '<input type="submit" value="Enviar"></form>'
        
        if request.method == "POST":
            respuesta = request.POST.get("titulo")
            if respuesta:
                objeto = Usuario.objects.get(nombre= nombreUsuario)
                objeto.titulo = respuesta
                objeto.save()
            descrip = request.POST.get("descripcion")
            if descrip:
                objeto = Usuario.objects.get(nombre= nombreUsuario)
                objeto.comentario = descrip
                objeto.save()        


        usuario = Usuario.objects.get(nombre = nombreUsuario)     
        return render_to_response('usuario.html',{'Espacio': "<br/>",'titulo':usuario.titulo,'comentario': usuario.comentario,'lista': salida, 'mensaje':mensaje, 'admin': admin, 'logger': logger}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/noRegistrado")   


def paginaUsuario(request,nombreUsuario):
    (mensaje, admin, logger, request.user.username) = autenticacionUsuario(request)
    userName = Usuario.objects.get(nombre=nombreUsuario)
    listaActividades = userName.actividades.all()
    salida = ""
    for fila in listaActividades:
        salida += "<br/>" + "<br/>"
        salida += "Actividad" + "<br/>"
        salida += "Titulo: " + fila.titulo + "<br/>"
        salida += "Tipo: " + fila.tipo + "<br/>"
        salida += "Precio: " + fila.precio + "<br/>"
        salida += "Fecha: " + str(fila.fecha) + "<br/>"
        salida += "Hora: " + str(fila.hora) + "<br/>"
        salida += "Fecha Fin: " + str(fila.fechaFin) + "<br/>"
        salida += "Evento Largo: " + str(fila.eventoLargo) + "<br/>"
        salida += "<a href="+ fila.informacion + ">" + '+ info' + '</a>' + "<br/>"
        member = Membership.objects.get(contenido=fila, usuario=userName)
        fechaAct = member.fechaEleccion
        salida += "elegida en " + str(fechaAct) + "<br/>"
        salida += "<br/>"

    usuario = Usuario.objects.get(nombre = nombreUsuario)     
    return render_to_response('paginaUsuarios.html',{'titulo':usuario.titulo,'comentario': usuario.comentario,'lista': salida, 'mensaje':mensaje, 'admin': admin, 'logger': logger}, context_instance=RequestContext(request))
    
def NoRegistrado(request):
    salida = "***AYUDA LOGIN*** SI NO HAS INICIADO SESION TODAVIA, HAZ LOGIN."
    (mensaje, admin, logger, request.user.username) = autenticacionUsuario(request)
    return render_to_response('noRegistrado.html',{'lista': salida, 'mensaje':mensaje, 'admin': admin, 'logger': logger}, context_instance=RequestContext(request))


def GuardarActividad(request,recurso):
    if request.user.is_authenticated():
        hoy = date.today()
        fechaHoy = str(hoy)
        iden = int(recurso) - 1 
        (mensaje, admin, logger, request.user.username) = autenticacionUsuario(request)
        nombreUsuario = request.user.username
        contenidos = Contenidos.objects.all()
        userName = Usuario.objects.get(nombre=nombreUsuario)
        m1 = Membership(contenido=contenidos[iden], usuario=userName,
                      fechaEleccion= fechaHoy)
        m1.save()
        todas = "/todas"
    return HttpResponseRedirect(todas)

def autenticacionUsuario(request):
    if request.user.is_authenticated():
        mensaje = "Tu usuario es: " + request.user.username + "<br/>"
        admin = "/logout"
        logger = "Logout"
    else:
        mensaje = "No registrado,inicie sesion" + "<br/>"
        admin = "/login"
        logger = "Login"
    return (mensaje, admin, logger, request.user.username)

def rss(request):
    if request.user.is_authenticated():
        (mensaje, admin, logger, request.user.username) = autenticacionUsuario(request)
        nombreUsuario = request.user.username
        userName = Usuario.objects.get(nombre=nombreUsuario)
        listaActividades = userName.actividades.all()

        salida =  '<?xml version="1.0" encoding="ISO-8859-1" ?>\n'+\
                  '<rss version="2.0">\n'+\
                  '\t<channel>\n'+\
                  '\t\t<title>RSS del usuario</title>\n'
        for fila in listaActividades:
            salida += '\t<item>\n'
            salida += '\t\t<Titulo>'+ fila.titulo + '</Titulo>\n'
            salida += '\t\t<Tipo>'+ fila.tipo + '</Tipo>\n'
            salida += '\t\t<Precio>'+ fila.precio + '</Precio>\n'
            salida += '\t\t<Fecha>'+ fila.fecha + '</Fecha>\n'
            salida += '\t\t<Hora>'+ fila.hora + '</Hora>\n'
            salida += '\t\t<FechaFin>'+ fila.fechaFin + '</FechaFin>\n'
            salida += '\t\t<EventoLargo>'+ str(fila.eventoLargo) + '</EventoLargo>\n'
            salida += '\t</item>'

        return HttpResponse(salida + "\t </channel>\n</rss>\n", content_type = 'rss')
    else:
        return HttpResponseRedirect('/noRegistrado')

def rssUsuario(request,usuario):
    userName = Usuario.objects.get(nombre=usuario)
    listaActividades = userName.actividades.all()
    
    salida =  '<?xml version="1.0" encoding="ISO-8859-1" ?>\n'+\
              '<rss version="2.0">\n'+\
              '\t<channel>\n'+\
              '\t\t<title>RSS del usuario</title>\n'
    for fila in listaActividades:
        salida += '\t<item>\n'
        salida += '\t\t<Titulo>'+ fila.titulo + '</Titulo>\n'
        salida += '\t\t<Tipo>'+ fila.tipo + '</Tipo>\n'
        salida += '\t\t<Precio>'+ fila.precio + '</Precio>\n'
        salida += '\t\t<Fecha>'+ fila.fecha + '</Fecha>\n'
        salida += '\t\t<Hora>'+ fila.hora + '</Hora>\n'
        salida += '\t\t<FechaFin>'+ fila.fechaFin + '</FechaFin>\n'
        salida += '\t\t<EventoLargo>'+ str(fila.eventoLargo) + '</EventoLargo>\n'
        salida += '\t</item>'

    return HttpResponse(salida + "\t </channel>\n</rss>\n", content_type = 'rss')
    

@csrf_exempt
def login_view(request):
    form ='<form action="" method="POST" accept-charset="UTF-8">' +\
          'username: <input type="text" name="username">' +\
          'password: <input type="password" name="password">' +\
          '<input type="submit" value="Login"></form>'+\
          '<br/>'
    if request.method == 'POST':       
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
               if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                return render_to_response('noUsuario.html', context_instance=RequestContext(request))
    return render_to_response('login.html',{'form': form}, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')





