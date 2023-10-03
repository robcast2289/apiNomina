from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json
from models.StatusEmpleadoModel import StatusEmpleadoModel
from models.InasistenciaModel import InasistenciaModel
from models.PeriodoPlanillaModel import PeriodoPlanillaModel
from schemas.NominaSchemas import *


router = APIRouter(
    prefix="/nomina",
    #tags=["Nomina"],
)



# StatusEmpleado
routerStatusEmpleado = APIRouter(
    tags=["StatusEmpleado"],
)

@routerStatusEmpleado.get('/statusempleado')
async def statusempleado_get():
    statusempleado = StatusEmpleadoModel.ObtenerTodosStatusEmpleado()
    return statusempleado

@routerStatusEmpleado.put("/statusempleado/{IdUsuario}")
async def statusempleado_put(IdUsuario,model:StatusEmpleadoRequest):
    StatusEmpleadoModel.InsertarStatusEmpleado(model,IdUsuario)
    return

@routerStatusEmpleado.delete("/statusempleado/{IdStatusEmpleado}")
async def statusempleado_delete(IdStatusEmpleado):
    ret = StatusEmpleadoModel.EliminarStatusEmpleado(IdStatusEmpleado)
    return ret

@routerStatusEmpleado.post("/statusempleado/{IdUsuario}/{IdStatusEmpleado}")
async def statusempleado_post(IdUsuario,IdStatusEmpleado,model:StatusEmpleadoRequest):
    ret = StatusEmpleadoModel.ActualizarStatusEmpleado(model,IdUsuario,IdStatusEmpleado)
    print(ret)
    return ret



# Inasistencia
routerInasistencia = APIRouter(
    tags=["Inasistencia"],
)

@routerInasistencia.get('/inasistencia')
async def inasistencia_get():
    inasistencia = InasistenciaModel.ObtenerTodosInasistencia()
    return inasistencia

@routerInasistencia.put("/inasistencia/{IdUsuario}")
async def inasistencia_put(IdUsuario,model:InasistenciaRequest):
    InasistenciaModel.InsertarInasistencia(model,IdUsuario)
    return

@routerInasistencia.delete("/inasistencia/{IdInasistencia}")
async def inasistencia_delete(IdInasistencia):
    ret = InasistenciaModel.EliminarInasistencia(IdInasistencia)
    return ret

@routerInasistencia.post("/inasistencia/{IdUsuario}/{IdInasistencia}")
async def inasistencia_post(IdUsuario,IdInasistencia,model:InasistenciaRequest):
    ret = InasistenciaModel.ActualizarInasistencia(model,IdUsuario,IdInasistencia)
    print(ret)
    return ret



# PeriodoPlanilla
routerPeriodoPlanilla = APIRouter(
    tags=["PeriodoPlanilla"],
)

@routerPeriodoPlanilla.get('/periodoplanilla')
async def periodoplanilla_get():
    periodoplanilla = PeriodoPlanillaModel.ObtenerTodosPeriodoPlanilla()
    return periodoplanilla

@routerPeriodoPlanilla.put("/periodoplanilla/{IdUsuario}")
async def periodoplanilla_put(IdUsuario,model:PeriodoPlanillaRequest):
    PeriodoPlanillaModel.InsertarPeriodoPlanilla(model,IdUsuario)
    return

@routerPeriodoPlanilla.delete("/periodoplanilla/{IdPeriodoPlanilla}")
async def periodoplanilla_delete(IdPeriodoPlanilla):
    ret = PeriodoPlanillaModel.EliminarPeriodoPlanilla(IdPeriodoPlanilla)
    return ret

#@routerPeriodoPlanilla.post("/periodoplanilla/{IdUsuario}/{IdPeriodoPlanilla}")
#async def periodoplanilla_post(IdUsuario,IdPeriodoPlanilla,model:PeriodoPlanillaRequest):
#    ret = PeriodoPlanillaModel.ActualizarPeriodoPlanilla(model,IdUsuario,IdPeriodoPlanilla)
#    print(ret)
#    return ret


router.include_router(routerStatusEmpleado)
router.include_router(routerInasistencia)
router.include_router(routerPeriodoPlanilla)