from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class StatusEmpleadoRequest(BaseModel):
    Nombre:str


class InasistenciaRequest(BaseModel):
    IdEmpleado:int
    FechaInicial:datetime
    FechaFinal:datetime
    MotivoInasistencia:str


class PeriodoPlanillaRequest(BaseModel):
    Anio:int
    Mes:int
    Cantidad:int