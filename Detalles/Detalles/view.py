from django.http import HttpResponse
from django.template import Template, Context
import datetime

class material(object):
    def __init__(self, ciclo, name):
        self.ciclo=ciclo
        self.name=name

def hello(request): #first view
    #Nombres de las materias
    clases=material('II', 'Calculus')
    courses=['Single Variable', 'Vetors', 'Derivarites', 'Integers', 'Limits & Continuity']
    time=datetime.datetime.now()
    name='Wilder Julcahunca More'
    HomeFile=open('/home/sarah/Documents/Programing/WebDjango/Detalles/Detalles/Plantillas/Home.html')
    plt=Template(HomeFile.read())
    HomeFile.close()
    ctx=Context({'fecha':time.date, 'names':name, 'clases':clases.ciclo, 'materia':clases.name, 'temas':courses})
    document=plt.render(ctx)
    return HttpResponse(document)