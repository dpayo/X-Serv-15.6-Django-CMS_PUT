from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from models import Table

# Create your views here.

@csrf_exempt
def analyze (request,recurso):
    
    if request.method == 'GET':
        try:
            record = Table.objects.get(resource=recurso)
            return HttpResponse(record.name)
        except Table.DoesNotExist:
            return HttpResponseNotFound('Page not found:')
        
    elif request.method == 'PUT':
        record = Table(resource= recurso,name =request.body)  
        record.save()
        return HttpResponse('<h1>Actualizando.../h1>'+ request.body)
   
