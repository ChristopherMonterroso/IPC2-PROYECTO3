from flask  import Flask,request
from flask.json import jsonify
from flask_cors import CORS
from gestor import Gestor
from xml.etree import ElementTree as ET
from DateTime import Timezones
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

@app.route('/abrirAutor',methods=['GET'])
def getAutor():
    gestor.abrirAutor()
    return jsonify({'mensaje':"Archivo abierto"})
    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=3000,debug=True)