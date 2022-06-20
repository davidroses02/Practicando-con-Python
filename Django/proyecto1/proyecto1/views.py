from datetime import datetime
from django.template import Template, Context
from django.http import HttpResponse
import datetime

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# cada función dentro del archivo views.py es una vista
def saludo(request):

    p1 = Persona("David", "Rosas")
    temasGenerales = ["Platzi", "Django", "Programación"]
    doc_externo = open("C:/Users/david/Documents/Practicando-con-Python/Django/proyecto1/proyecto1/plantillas/miplantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre": p1.nombre, "apellido": p1.apellido, "temas": temasGenerales}) 
    documento = plt.render(ctx)
    return HttpResponse(documento)

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