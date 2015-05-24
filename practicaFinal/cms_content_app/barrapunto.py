#!/usr/bin/python
# -*- encoding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
from models import Contenidos
from models import Usuario
from models import FechaActualizacion
from models import Membership

class CounterHandler(ContentHandler):

    def __init__ (self):
        self.salida = ""
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.Atributos = ""
        self.titulo = ""
        self.tipo = ""
        self.precio = ""
        self.fecha = ""
        self.hora = ""
        self.finEvento = ""
        self.eventoLargo = ""
        self.informacion = ""

    def startElement (self, name, attrs):
        if name == 'contenido':
            self.inItem = True
        elif self.inItem:
            if name == 'atributo':
                self.inContent = True
                self.Atributos = attrs['nombre']
                
    def endElement (self, name):
        if name == 'contenido':
            self.inItem = False
        elif self.inItem:
            if name == 'atributo' and self.Atributos == 'TITULO':
                self.salida+= "Titulo: " + self.theContent + "."
                self.salida+= ""
                self.titulo = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == 'atributo' and self.Atributos == 'TIPO':
                self.salida+= "Tipo: " + self.theContent + "."
                self.salida+= ""
                self.tipo = self.theContent
                lista = Contenidos.objects.all()
                Encontrado = False
                for fila in lista:
                    if fila.titulo == self.titulo:
                        Encontrado = True
                        
                if not Encontrado:
                    contenido = Contenidos(titulo=self.titulo, tipo=self.tipo, precio= self.precio,
                                    fecha= self.fecha, hora= self.hora, fechaFin = self.finEvento,
                                     eventoLargo= self.eventoLargo,informacion= self.informacion)
                    contenido.save()
                self.inContent = False
                self.theContent = ""
            elif name == 'atributo' and self.Atributos == 'PRECIO':
                self.salida+= "Precio: " + self.theContent + "."
                self.salida+= ""
                self.precio = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == 'atributo' and self.Atributos == 'FECHA-EVENTO':
                self.salida+= "Fecha: " + self.theContent + "."
                self.salida+= ""
                self.fecha = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == 'atributo' and self.Atributos == 'HORA-EVENTO':
                self.salida+= "Hora: " + self.theContent + "."
                self.salida+= ""
                self.hora = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == 'atributo' and self.Atributos == 'FECHA-FIN-EVENTO':
                self.salida+= "Duracion: " + self.theContent + "."
                self.salida+= ""
                self.finEvento = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == 'atributo' and self.Atributos == 'EVENTO-LARGA-DURACION':
                self.salida+= "Evento Larga Duracion: " + self.theContent + "."
                self.salida+= ""
                self.eventoLargo = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == 'atributo' and self.Atributos == 'CONTENT-URL-ACTIVIDAD':
                print self.theContent
                self.salida+= "Contenido Actividad: " + self.theContent
                self.salida+= ""
                
                self.informacion = self.theContent
                self.inContent = False
                self.theContent = ""

    def characters (self, chars):
    
        if self.inContent:
            if self.Atributos == 'CONTENT-URL-ACTIVIDAD':
                self.theContent += chars
            else:
                self.theContent = chars
        
                
def getBarrapunto():       
    # Load parser and driver

    JokeParser = make_parser()
    JokeHandler = CounterHandler()
    JokeParser.setContentHandler(JokeHandler)

    # Ready, set, go!
    JokeParser.parse("http://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3"+
            "c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&"+
            "format=xml&file=0&filename=206974-0-agenda-eventos-culturales-100&mgmtid="+
            "6c0b6d01df986410VgnVCM2000000c205a0aRCRD")

    return JokeHandler.salida
