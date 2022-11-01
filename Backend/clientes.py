class Clientes:
    def __init__(self,nit,nombre,usuario,clave,direccion,email) -> None:
        self.nit=nit
        self.nombre=nombre
        self.usuario=usuario
        self.clave=clave
        self.direccion=direccion
        self.email=email
        self.lista_instancias=[]

class Instancias:
    def __init__(self,id_instancia,id_configuracion,nombre,fechaInicio,estado,fechaFinal) -> None:
        self.id_instancia=id_instancia
        self.id_configuracion=id_configuracion
        self.nombre=nombre
        self.fechaIinicio=fechaInicio
        self.estado=estado
        self.fechaFinal=fechaFinal