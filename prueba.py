import xml.etree.ElementTree as ET
import re

expresion="^(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[1-2])\1\d{4}$"

x="esta es una descripcion de la fecha 22/02/2016, 22/03/2020"
s = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
fecha = s.search(x)

try:
    print(fecha)
except:
    print("N/A")


"""for recursos in archivo[0]:
    print("ID:",recursos.attrib['id'])
    print("Nombre:",recursos[0].text)
    print("Abreviatura:",recursos[1].text)
    print("Metrica:",recursos[2].text)
    print("Tipo:",recursos[3].text)
    print("Valor/hora:",recursos[4].text)
        #print(lista_recursos)
for categorias in archivo[1]:
    print(categorias.attrib['id'])
    print(categorias[0].text)
    print(categorias[1].text)
    print(categorias[2].text)
    for Configuracion in categorias[3]:
        print(Configuracion.attrib['id'])
        print(Configuracion[0].text)
        print(Configuracion[1].text)
        for recursosConfig in Configuracion[2]:
            print(recursosConfig.attrib['id'],"--",recursosConfig.text)
for clientes in archivo[2]:
    print(clientes.attrib['nit'])
    print(clientes[0].text)#nombre
    print(clientes[1].text)#usuario
    print(clientes[2].text)#clave
    print(clientes[3].text)#direccion
    print(clientes[4].text)#correo
    for instancia in clientes[5]:
        print(instancia.attrib['id'])
        print(instancia[0].text)
        print(instancia[1].text)
        print(instancia[2].text)
        print(instancia[3].text)
        print(instancia[4].text)"""