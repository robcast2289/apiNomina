from pydantic import BaseModel
from datetime import datetime

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


class UsuarioRequest(BaseModel):
    IdUsuario:str
    Nombre:str
    Apellido:str
    FechaNacimiento:datetime
    IdStatusUsuario:int
    IdGenero:int
    UltimaFechaIngreso:str
    IntentosDeAcceso:int
    SesionActual:str
    UltimaFechaCambioPassword:datetime
    CorreoElectronico:str
    RequiereCambiarPassword:int
    Fotografia:str
    TelefonoMovil:str
    IdSucursal:int