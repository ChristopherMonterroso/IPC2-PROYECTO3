import re
from categorias import configuracion,Categoria,recursosConfiguracion
from clientes import Clientes, Instancias
from consumos import Consumo
from recursos import Recursos
from facturas import factura
import os
import webbrowser
import datetime

class Gestor:
    def __init__(self) -> None:
        self.clientes = []
        self.categorias = []
        self.recursos= []
        self.consumos = []
        self.facturas=[]
        self.expresion="^(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[1-2])\1\d{4}$"

    def setRecursos(self,id, nombre,siglas,metrica,tipo,valorXhora):
        set = Recursos(id,nombre,siglas,metrica,tipo,valorXhora)
        self.recursos.append(set)

    def setCategoria(self,id,nombre,descripcion,cargaTrabajo):
        categoria= Categoria(id,nombre,descripcion,cargaTrabajo)
        self.categorias.append(categoria)

    def setConfiguracion(self,id_categoria,id_config,id_nombre,id_descripcion):
        config=configuracion(id_config,id_nombre,id_descripcion)
        for i in self.categorias:
            if id_categoria==i.id:
                i.configuraciones.append(config)
    
    def setRecurosConfig(self,id_categoria,id_config,id,cantidad):
        rec=recursosConfiguracion(id,cantidad)
        for i in self.categorias:
            if id_categoria==i.id:
                for j in i.configuraciones:
                    if id_config==j.id:
                        j.recursosConfiguracion.append(rec)
    
    def setCliente(self,nit,nombre,usuario,clave,direccion,email):
        cliente=Clientes(nit,nombre,usuario,clave,direccion,email)
        self.clientes.append(cliente)

    def setInstancias(self,nit,id_i,id_c,nombre,fechaInicio,estado,fechafinal):
        s = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
        fecha_inicial = s.search(fechaInicio)
        fecha_final=""
        fecha_final= s.search(fecha_final)
        try:
            fecha_final=fecha_final.group()
        except:
            fecha_final="N/A"
        instancia=Instancias(id_i,id_c,nombre,fecha_inicial.group() ,estado,fecha_final)
        for i in self.clientes:
            if nit==i.nit:
                i.lista_instancias.append(instancia)
    
    def setConsumos(self,nit,id,tiempo,fechaHora):
        s = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
        fechaHora= s.search(fechaHora)
        tiempo= tiempo.replace(" ","")
        consumo=Consumo(nit,id,tiempo,fechaHora.group())
        self.consumos.append(consumo)

    def consultarDatos(self):
        json=[]
        for i in self.recursos:
            recurso={
                'Datos':'Recursos',
                'id':i.id_recurso,
                'nombre':i.nombre,
                'abreviatura':i.abreviatura,
                'metrica':i.metrica,
                'tipo':i.tipo,
                'valor/hora':i.valor_x_hora
            }
            json.append(recurso)
        for i in self.categorias:
            categoria={
                'Datos':'Categorias',
                'id':i.id,
                'nombre':i.nombre,
                'descripcion':i.descripcion,
                'carga de Trabajo':i.cargaTrabajo
            }
            json.append(categoria)
            for j in i.configuraciones:
                config={
                'Datos':'Configuraciones',
                'id':j.id,
                'nombre':j.nombre,
                'descripcion':j.descripcion
            }
                json.append(config)
                for s in j.recursosConfiguracion:
                    rec={
                        'Datos':'Configuracion del recurso',
                        'id':s.id,
                        'cantidad':s.cantidad
                    }
                    json.append(rec)
        for i in self.clientes:
            cliente={
                'Datos':'Cliente',
                'id':i.nit,
                'nombre':i.nombre,
                'usuario':i.usuario,
                'clave':i.clave,
                'direccion':i.direccion,
                'email':i.email
            }
            json.append(cliente)
            for j in i.lista_instancias:
                if j.estado==" Activa ":
                    instancia={
                        'Datos':'Instancia',
                        'id instancia':j.id_instancia,
                        'id configuracion':j.id_configuracion,
                        'nombre':j.nombre,
                        'fecha inicio':j.fechaInicio,
                        'estado':j.estado,
                        'fecha final':j.fechaFinal
                    }
                    json.append(instancia)
        return json

    def getConsumos(self):
        json=[]
        for i in self.consumos:
            consumo={
                'nit':i.nit,
                'id instancia':i.id_instancia,
                'tiempo':i.tiempo,
                'fecha Hora':i.fechaHora
            }
            json.append(consumo)
        return json
    def getCategorias(self):
        json=[]
        for i in self.categorias:
            categoria={
                'Datos':'Categorias',
                'id':i.id,
                'nombre':i.nombre,
                'descripcion':i.descripcion,
                'carga_de_Trabajo':i.cargaTrabajo
            }
            json.append(categoria)
        return json
    def getRecursos(self):
        json=[]
        for i in self.recursos:
            recurso={
                'id':i.id_recurso,
                'nombre':i.nombre,
                'abreviatura':i.abreviatura,
                'metrica':i.metrica,
                'tipo':i.tipo,
                'valorxhora':i.valor_x_hora
            }
            json.append(recurso)
        return json

    def getClientes(self):
        json=[]
        for i in self.clientes:
            cliente={
                'Datos':'Cliente',
                'id':i.nit,
                'nombre':i.nombre,
                'usuario':i.usuario,
                'clave':i.clave,
                'direccion':i.direccion,
                'email':i.email
            }
            json.append(cliente)
            for j in i.lista_instancias:
                if j.estado==" Activa ":
                    instancia={
                        'Datos':'Instancia',
                        'id_instancia':j.id_instancia,
                        'id_configuracion':j.id_configuracion,
                        'i_nombre':j.nombre,
                        'fecha_inicio':j.fechaInicio,
                        'estado':j.estado,
                        'fechafinal':j.fechaFinal
                    }
                    json.append(instancia)
        
        return json
    
    
    def getFacturas(self,inicio,final):
        monto=0
        
        rango=inicio.split("/")
        fecha1=datetime.date(int(rango[2]),int(rango[1]),int(rango[0]))  
        rango_final=final
        rango_2=rango_final.split("/")
        fecha2=datetime.date(int(rango_2[2]),int(rango_2[1]),int(rango_2[0]))
        for i in self.consumos:
            fecha_c=i.fechaHora
            fecha_numero=fecha_c.split("/")
            fecha_consumo=datetime.date(int(fecha_numero[2]),int(fecha_numero[1]),int(fecha_numero[0]))
            tiempoi=i.tiempo
            tiempo=tiempoi.split(".")
            if fecha_consumo>=fecha1 and fecha_consumo<=fecha2:
                print("Factura")
                for j in self.clientes:
                    if j.nit == i.nit:
                        usuario=j
                print("NIT:",usuario.nit)
                for  l in usuario.lista_instancias:
                    if l.id_instancia==i.id_instancia:
                        instancia=l
                print("instancia: ",instancia.id_instancia)
                for c in self.categorias:
                    print(c.nombre)
    def getFacturaDetalle(self):
        pass
    
    def getFacturaAnalisis(self):
        pass
    def abrirAutor(self):
        webbrowser.open_new_tab("file:///"+os.getcwd()+"/Documentacion/Autor.pdf")
