from pydantic import BaseModel

class ModuloRequest(BaseModel):
    Nombre:str
    OrdenMenu:int


class MenuRequest(BaseModel):
    IdModulo:int
    Nombre:str
    OrdenMenu:int


class OpcionRequest(BaseModel):
    IdMenu:int
    Nombre:str
    OrdenMenu:int
    Pagina:str


class RoleRequest(BaseModel):
    Nombre:str


class RoleOpcionRequest(BaseModel):
    IdRole:int
    IdOpcion:int
    Alta:int
    Baja:int
    Cambio:int
    Imprimir:int
    Exportar:int