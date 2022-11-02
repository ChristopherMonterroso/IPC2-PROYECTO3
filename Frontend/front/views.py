from django.shortcuts import render
from .forms import *
# Create your views here.
import requests

endpoint="http://127.0.0.1:3000/"

def index(request):
    context={
        'title':'index'
    }
    return render(request,'index.html',context)

def verRecursos(request):
    contexto = {
        'recursos' : []
    }
    
    try:
        response = requests.get(endpoint + 'verRecursos') 
        recursos=response.json()
        contexto['recursos']=recursos
    except:
        print('Error en la API')   
    return render(request, 'datos.html', contexto)
    
def verClientes(request):
    contexto={
        'clientes' : []
    }
    try:
        response=requests.get(endpoint+ 'getClientes')
        clientes=response.json()
        contexto['clientes']=clientes
        
    except:
        print('Error en la API clientes')
    return render(request, 'datos2.html', contexto)

def verCategorias(request):
    contexto={
        'categorias' : []
    }
    try:
        response=requests.get(endpoint+ 'getCategorias')
        categorias=response.json()
        contexto['categorias']=categorias
        
    except:
        print('Error en la API Categorias')
    return render(request, 'datos3.html', contexto)

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
            response = requests.post(endpoint + 'agregarConfiguraciones', data=xml_binary)
            if response.ok:
                ctx['response'] = 'Archivo XML cargado correctamente'
            else:
                ctx['response'] = 'Error en el servidor'
    else:
        return render(request, 'carga.html')
    return render(request, 'carga.html', ctx)

def cargaMasiva2(request):
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
            response = requests.post(endpoint + 'agregarConsumos', data=xml_binary)
            if response.ok:
                ctx['response'] = response
            else:
                ctx['response'] = 'Error en el servidor'
    else:
        return render(request, 'cargaConsumo.html')
    return render(request, 'cargaConsumo.html', ctx)

def addRecurso(request):
    if request.method == 'POST':
        form = AddFormRecurso(request.POST)
        if form.is_valid():
            json_data = form.cleaned_data
            response = requests.post(endpoint + 'crearRecurso', json=json_data)
            if response.ok:
                return render(request, 'Create.html', {'form':form})
        return render(request, 'Create.html', {'form':form})
    return render(request, 'Create.html')

def addCategoria(request):
    if request.method == 'POST':
        form = AddFormCategoria(request.POST)
        if form.is_valid():
            json_data = form.cleaned_data
            response = requests.post(endpoint + 'crearCategoria', json=json_data)
            if response.ok:
                return render(request, 'CreateCa.html', {'form':form})
        return render(request, 'CreateCa.html', {'form':form})
    return render(request, 'CreateCa.html')

def addConfiguracion(request):
    if request.method == 'POST':
        form = AddFormConfiguracion(request.POST)
        if form.is_valid():
            json_data = form.cleaned_data
            response = requests.post(endpoint + 'crearConfiguracion', json=json_data)
            if response.ok:
                return render(request, 'createconfig.html', {'form':form})
        return render(request, 'createconfig.html', {'form':form})
    return render(request, 'createconfig.html')

def addCliente(request):
    if request.method == 'POST':
        form = AddFormCliente(request.POST)
        if form.is_valid():
            json_data = form.cleaned_data
            response = requests.post(endpoint + 'crearCliente', json=json_data)
            if response.ok:
                return render(request, 'Createcliente.html', {'form':form})
        return render(request, 'Createcliente.html', {'form':form})
    return render(request, 'Createcliente.html')

def addInstancia(request):
    if request.method == 'POST':
        form = AddFormInstancia(request.POST)
        if form.is_valid():
            json_data = form.cleaned_data
            response = requests.post(endpoint + 'crearInstancia', json=json_data)
            if response.ok:
                return render(request, 'CrearIns.html', {'form':form})
        return render(request, 'CrearIns.html', {'form':form})
    return render(request, 'CrearIns.html')