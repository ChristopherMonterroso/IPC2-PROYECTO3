from flask  import Flask,request
from flask.json import jsonify
from flask_cors import CORS
import re
import datetime
from gestor import Gestor
from xml.etree import ElementTree as ET
from DateTime import Timezones
from fpdf import FPDF
from facturas import factura
class PDF(FPDF):
    def texts(self,name):
        with open(name,"rb") as xy:
            txt=xy.read().decode('latin-1')
        self.set_xy(10.0,80.0)
        self.set_text_color(68,50,50)
        self.set_font('Arial',"",12)
        self.multi_cell(0,10,txt)

    def titles(self,title):
        self.set_xy(0.0,0.0)
        self.set_font('Arial','B',16)
        self.set_text_color(220,50,50)
        self.cell(w=210.0,h=40.0,align="C",txt=title,border=0)
        

app=Flask(__name__)
app.config['DEBUG']=True
CORS(app)
gestor=Gestor()
@app.route('/agregarConfiguraciones',methods=['post'])
def agregarConfiguraciones():
    contClientes=0
    contInstancias=0
    try:
        xml=request.data.decode('utf-8')
        archivo=ET.XML(xml)
        for recursos in archivo[0]:
            gestor.setRecursos(recursos.attrib['id'],recursos[0].text,recursos[1].text,recursos[2].text,recursos[3].text,recursos[4].text)
        for categorias in archivo[1]:
            gestor.setCategoria(categorias.attrib['id'],categorias[0].text,categorias[1].text,categorias[2].text)
            for configuracion in categorias[3]:
                gestor.setConfiguracion(categorias.attrib['id'],configuracion.attrib['id'],configuracion[0].text,configuracion[1].text,)
                for recursosConfig in configuracion[2]:
                    gestor.setRecurosConfig(categorias.attrib['id'],configuracion.attrib['id'],recursosConfig.attrib['id'],recursosConfig.text)
        for clientes in archivo[2]:
            gestor.setCliente(clientes.attrib['nit'],clientes[0].text,clientes[1].text,clientes[2].text,clientes[3].text,clientes[4].text)
            for instancia in clientes[5]:  
                gestor.setInstancias(clientes.attrib['nit'],instancia.attrib['id'],instancia[0].text,instancia[1].text,instancia[2].text,instancia[3].text,instancia[4].text)   
                contInstancias+=1
            contClientes+=1
            print({
              "Archivo": "cargado exitosamente",
              "Clientes creados":contClientes,
              "Instancias creadas":contInstancias
            })
        return jsonify(
            {"Archivo": "cargado exitosamente",
              "Clientes creados":contClientes,
              "Instancias creadas":contInstancias
        })
    except:
        return jsonify({
            "Archivo":"ERROR"
        })


@app.route('/agregarConsumos', methods=['POST'])
def agregarConsumos():
    contConsumo=0
    try:
        xml=request.data.decode('utf-8')
        archivo=ET.XML(xml)
        for consumo in archivo:
            gestor.setConsumos(consumo.attrib['nitCliente'],consumo.attrib['idInstancia'],consumo[0].text,consumo[1].text)
            contConsumo+=1

        return jsonify({
            "archivo":"Cargado exitosamente",
            "consumos procesados":contConsumo
        })
    except:
        return jsonify({
            "Archivo":"ERROR"
        })

@app.route('/crearRecurso',methods=['POST'])
def setRecurso():
    json=request.get_json()
    gestor.setRecursos(json['id_recurso'],json['nombre'],json['abreviatura'],json['metrica'],json['tipo'],json['valor_x_hora'])
    return jsonify({ 'Recuros':'Cargado exitosamente'}),200

@app.route('/crearCategoria',methods=['POST'])
def setCategoria():
    json=request.get_json()
    gestor.setCategoria(json['id'],json['nombre'],json['descripcion'],json['cargaTrabajo'])
    return jsonify({ 'Categoria':'Cargada exitosamente'}),200

@app.route('/crearConfiguracion',methods=['POST'])
def setConfiguracion():
    json=request.get_json()
    gestor.setConfiguracion(json['id_categoria'],json['id'],json['nombre'],json['descripcion'])
    return jsonify({ 'categoria':'Cargada exitosamente'}),200

@app.route('/crearCliente',methods=['POST'])
def setCliente():
    json=request.get_json()
    gestor.setCliente(json['nit'],json['nombre'],json['usuario'],json['clave'],json['direccion'],json['email'])
    return jsonify({ 'Cliente':'Cargado exitosamente'}),200

@app.route('/crearInstancia',methods=['POST'])   
def setInstancia():
    json=request.get_json()
    gestor.setInstancias(json['nit'],json['id_i'],json['id_c'],json['nombre'],json['fechaInicio'],json['estado'],json['fechafinal'])
    return jsonify({ 'Instancia':'Cargada exitosamente'}),200

@app.route('/verRecursos',methods=['GET'])
def getRecursos():
    recursos=gestor.getRecursos()
    return jsonify(recursos),200

@app.route('/getClientes',methods=['GET'])
def getClientes():
    clientes=gestor.getClientes()
    return jsonify(clientes),200

@app.route('/getCategorias',methods=['GET'])
def getCategorias():
    clientes=gestor.getCategorias()
    return jsonify(clientes),200
@app.route('/getConsumos',methods=['GET'])
def getConsumos():
    clientes=gestor.getConsumos()
    return jsonify(clientes),200
@app.route('/consultarDatos',methods=['GET'])
def getDatos():
    recursos=gestor.consultarDatos()
    return jsonify(recursos),200

@app.route('/generarFacturaDetalle',methods=['GET'])
def getFacturaDetalle():
    gestor.getFacturaDetalle()
@app.route('/generarFacturaAnalisis',methods=['GET'])
def getFacturaAnalisis():
    gestor.getFacturaAnalisis()

@app.route("/generarFacturas",methods=['POST'])
def getFacuta():
    facturas=1
    json=request.get_json()
    Existe=False
    contenido=""
    monto=0
    rango_inicial=json['fechaInicial']
    rango=rango_inicial.split("/")
    fecha1=datetime.date(int(rango[2]),int(rango[1]),int(rango[0]))  
    rango_final=json['fechaFinal']
    rango_2=rango_final.split("/")
    fecha2=datetime.date(int(rango_2[2]),int(rango_2[1]),int(rango_2[0]))
    consumos = gestor.consumos
    clientes= gestor.clientes
    categorias= gestor.categorias
    recuros= gestor.recursos
    for i in consumos:
        fecha_c=i.fechaHora
        fecha_numero=fecha_c.split("/")
        fecha_consumo=datetime.date(int(fecha_numero[2]),int(fecha_numero[1]),int(fecha_numero[0]))
        tiempoi=i.tiempo
        
        if fecha_consumo>=fecha1 and fecha_consumo<=fecha2:
            numero=str(facturas)
            contenido+="Factura: "+str(facturas)
            for j in clientes:
                if j.nit == i.nit:
                    usuario=j
            contenido+="\nNIT: "+usuario.nit
            nit=usuario.nit
            for  l in usuario.lista_instancias:
                if l.id_instancia==i.id_instancia:
                    instancia=l
            contenido+="\nFecha: "+str(fecha_consumo)
            cns=str(fecha_consumo)
            for c in categorias:
                instancia.id_configuracion= instancia.id_configuracion.replace(" ","")
                for confi in c.configuraciones:
                    if(confi.id ==instancia.id_configuracion):
                      
                        configuracion=confi
            for r in configuracion.recursosConfiguracion:
                for r2 in recuros:
                    if r.id==r2.id_recurso:
                        aporte=(float(r2.valor_x_hora))*float(tiempoi)*float(r.cantidad)
                        monto=monto + aporte
            contenido+="\nMonto a pagar: "+str(monto)+"\n"
            gestor.facturas.append(factura(numero,nit,cns,monto))
        facturas+=1
        monto=0
    ruta= open("facturas.txt",'w')
    ruta.write(contenido)
    ruta.close()
    pdf = PDF()
    pdf.add_page()
    pdf.titles("Facturas")
    pdf.texts("facturas.txt")
    pdf.output("Facturas.pdf")
    return jsonify({"mensaje":"Facturas generadas"})

@app.route("/reporteRecursos", methods=['GET'])
def reportRecur():
    lista = gestor.recursos

    contenido=""
    for r in lista:
        contenido+="ID:"+str(r.id_recurso)+"\n"
        contenido+="Nombre: "+str(r.nombre)+"\n"
        contenido+="Monto:" +str(r.valor_x_hora)+"\n"

    ruta= open("rec.txt",'w')
    ruta.write(contenido)
    ruta.close()
    pdf = PDF()
    pdf.add_page()
    pdf.titles("Recrusos con mas ingresos")
    pdf.texts("rec.txt")
    pdf.output("Recursos.pdf")
    return jsonify({"mensaje":"PDF generado"})
@app.route("/getFactura",methods=['POST'])
def factur():
    json=request.get_json()
    contenido= ""
    nFactura=json["factura:"]
    facturas = gestor.facturas
    for i in facturas:
        if nFactura==i.numero:
            contenido+="Factura"+str(i.numero)+"\nNit del cliente: "+str(i.nit)+"\nFecha de consumo:"+str(i.fecha)+"\n Monto a pagar:"+str(i.monto)
    ruta= open("factura.txt",'w')
    ruta.write(contenido)
    ruta.close()
    pdf = PDF()
    pdf.add_page()
    pdf.titles("Factura")
    pdf.texts("factura.txt")
    pdf.output("Factura.pdf")
    return jsonify({"mensaje":"Factura generada"})






@app.route('/abrirAutor',methods=['GET'])
def getAutor():
    gestor.abrirAutor()
    return jsonify({'mensaje':"Archivo abierto"})
    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=3000,debug=True)