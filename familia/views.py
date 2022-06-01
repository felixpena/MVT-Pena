from django.http import HttpResponse
from .models import Persona
from django.template import loader
from django.shortcuts import render

# Método Rendering
def index(request):
    lista_persona = Persona.objects.all()
    context = {'lista_persona': lista_persona}
    return render(request, "familia/index.html", context)

"""
def index(request):
    lista_persona = Persona.objects.all()
    template = loader.get_template('familia/index.html')
    context = {
        'lista_persona': lista_persona,
    }
    return HttpResponse(template.render(context, request))
"""
def template1(request):
    return render(request, 'familia/template1.html')

def inicio(request):
    return HttpResponse(" BIENVENIDO")

"""
def index(request):
    lista_persona = Persona.objects.all()
    salida = lista_persona
    return HttpResponse(salida)
""" 
# Leave the rest of the views (detail, results, vote) unchanged

""" 
def index(request):
    return HttpResponse("Hello, world. You're at the familia index.")
"""

def detail(request, question_id):
    return HttpResponse("Estás viendo la pregunta %s." % question_id)

def results(request, question_id):
    response = "Estás viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Usted está votando sobre la pregunta %s." % question_id)