from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('paparazzi.html')
    template_render = template.render()
    return HttpResponse(template_render)

def famosos(request):
    template = loader.get_template('famosos.html')
    template_render = template.render()
    return HttpResponse(template_render)

def videos(request):
    template = loader.get_template('videos.html')
    template_render = template.render()
    return HttpResponse(template_render)