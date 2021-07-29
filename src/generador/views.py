from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from generador.generador import generar_pdf
from django.http import FileResponse
import json
#a function that returns a random string of length n
@csrf_exempt
def index(request):
    try:
        body=json.loads(request.body)
    except:
        return HttpResponse("Por favor haz un request post con el body correcto :)",status=403) 
    if request.method=='POST' and len(body)==5:
        try:
            carrera=body["carrera"]
            titulo=body["titulo"]
            curso=body["curso"]
            semestre=body["semestre"]
            alumnos=body["alumnos"]
            if len(alumnos)>6:
                return HttpResponse("Sólo se acepta hasta 6 alumnos.",status=403) 
            #Se ejecuta el generador con los argumentos listados anteriormente
            sems=''
            if semestre==1:
                sems='1er semestre'
            elif semestre==2:
                sems='2do semestre'
            elif semestre==3:
                sems='3er semestre'
            elif semestre==4:
                sems='4to semestre'
            elif semestre==5:
                sems='5to semestre'
            elif semestre==6:
                sems='6to semestre'
            elif semestre==7:
                sems='7mo semestre'
            elif semestre==8:
                sems='8vo semestre'
            elif semestre==9:
                sems='9no semestre'
            else:
                sems='10mo semestre'
            caratula=generar_pdf(carrera,titulo,curso,sems,alumnos)
            return HttpResponse(caratula
            ,status=200)
        except:
            return HttpResponse("Por favor haz un request post con el body correcto :)",status=403)
    return HttpResponse("Por favor haz un request post con el body correcto :)",status=403)

def retornar_caratula(request,id):
    try:
        pdf=open('./generador/pdfs/'+id+'.pdf','rb')
        response = FileResponse(pdf)
    except:
        return HttpResponse("No se encuentra el archivo",status=404)
    return response
# Create your views here.
