from datetime import datetime
from django.template import Template, Context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# cada función dentro del archivo views.py es una vista
def saludo(request):
    p1 = Persona("David", "Rosas")
    temasGenerales = ["Platzi", "Django", "Programación"]
    return render(request, "miplantilla.html", {
           "nombre": p1.nombre, "apellido": p1.apellido, "temas": temasGenerales})
    #doc_externo = loader.get_template('miplantilla.html') # mirar settings.py -> DIRS -> el directorio donde estan todas las plantillas

def cursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "cursoc.html", {"dameFecha": fecha_actual})

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
    <body>
    <p>
    Fecha y hora actuales: %s
    </p>
    </body>
    </html>
    """ % fecha_actual

    return HttpResponse(documento)

def calcularEdad(request, edad, agno):
    periodo = agno - 2022
    edadFutura = edad + periodo
    documento = """
    <html>
    <body>
    <p>
    En el año %s tendrás %s años
    </p>
    </body>
    </html>
    """ %(agno, edadFutura)

    return HttpResponse(documento)