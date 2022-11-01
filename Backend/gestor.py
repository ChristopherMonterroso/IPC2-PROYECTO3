from categorias import configuracion,Categoria,recursosConfiguracion
from clientes import Clientes, Instancias
from consumos import Consumo
from recursos import Recursos
class Gestor:
    def __init__(self) -> None:
        self.clientes = []
        self.categorias = []
        self.recursos= []
        self.consumos = []
    