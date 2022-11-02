from multiprocessing import context
from django.shortcuts import render
#from .forms import CrearRecurso
# Create your views here.
import requests

endpoint="http://127.0.0.1:3000/"

def index(request):
    context={
        'title':'index'
    }
    return render(request,'index.html',context)
def abrirAutor(request):
    try:
        response= requests.get(endpoint+"abrirAutor")
    except:
        print("ERROR EN LA API")
    context={
        'title':'index'
    }
    return render(request,'index.html',context)

def cargaMasiva(request):
    ctx = {
        'content':None,
        'response':None
    }
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            xml_binary = f.read()
            xml = xml_binary.decode('utf-8')
            ctx['content'] = xml
            response = requests.post(endpoint + 'agregarCanciones', data=xml_binary)
            if response.ok:
                ctx['response'] = 'Archivo XML cargado corrrectamente'
            else:
                ctx['response'] = 'Error en el servidor'
    else:
        return render(request, 'carga.html')
    return render(request, 'carga.html', ctx)