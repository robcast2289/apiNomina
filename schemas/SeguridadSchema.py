from pydantic import BaseModel

class ModuloRequest(BaseModel):
    Nombre:str
    OrdenMenu:int