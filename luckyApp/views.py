from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random
# Create your views here.

def suerteDiaria(requets): 
    signos = ["Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"]
    suertes = ["Buena", "Mala", "Regular"]

    suerte_signos = {}
    for signo in signos:
        suerte_signos[signo] = random.choice(suertes)

    template = loader.get_template('tabla.html')
    template_render = template.render({ 'suerte_signos': suerte_signos })
    return HttpResponse(template_render)