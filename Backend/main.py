from flask  import Flask,request
from flask.json import jsonify
from flask_cors import CORS
from gestor import Gestor
from xml.etree import ElementTree as ET

app=Flask(__name__)
app.config['DEBUG']=True
CORS(app)

@app.route('/agregarConfiguraciones',methods=['post'])
def agregarConfiguraciones():
    xml=request.data.decode('utf-8')
    raiz=ET.XML(xml)
        


if __name__=="__main__":
    app.run(debug=True)