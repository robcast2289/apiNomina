from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EstadoCivilRequest(BaseModel):
    Nombre:str


class TipoDocumentoRequest(BaseModel):
    Nombre:str


class DepartamentoRequest(BaseModel):
    Nombre:str
    IdEmpresa:int


class PuestoRequest(BaseModel):
    Nombre:str
    IdDepartamento:int