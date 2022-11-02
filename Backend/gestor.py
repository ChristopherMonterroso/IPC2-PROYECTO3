import re
from categorias import configuracion,Categoria,recursosConfiguracion
from clientes import Clientes, Instancias
from consumos import Consumo
from recursos import Recursos
import os
import webbrowser
class Gestor:
    def __init__(self) -> None:
        self.clientes = []
        self.categorias = []
        self.recursos= []
        self.consumos = []
    
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
        instancia=Instancias(id_i,id_c,nombre,fechaInicio,estado,fechafinal)
        for i in self.clientes:
            if nit==i.nit:
                i.lista_instancias.append(instancia)
    
    def setConsumos(self,nit,id,tiempo,fechaHora):
        consumo=Consumo(nit,id,tiempo,fechaHora)
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
    
    def getFacturaDetalle(self):
        pass
    
    def getFacturaAnalisis(self):
        pass
    def abrirAutor(self):
        webbrowser.open_new_tab("file:///"+os.getcwd()+"/Documentacion/Autor.pdf")
