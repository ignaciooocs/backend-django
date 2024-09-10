from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def secciones(request):
    template = loader.get_template('mainApp.html')
    template_render = template.render()
    return HttpResponse(template_render)