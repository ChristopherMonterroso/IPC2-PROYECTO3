class Categoria:
    def __init__(self,id,nombre,descripcion,cargaTrabajo) -> None:
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.cargaTrabajo=cargaTrabajo
        self.configuraciones=[]
class configuracion:
    def __init__(self,id,nombre,descripcion) -> None:
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.recursosConfiguracion=[]

class recursosConfiguracion:
    def __init__(self,id,cantidad) -> None:
        self.id=id
        self.cantidad=cantidad