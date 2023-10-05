from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import json
from models.StatusEmpleadoModel import StatusEmpleadoModel
from models.InasistenciaModel import InasistenciaModel
from models.PeriodoPlanillaModel import PeriodoPlanillaModel
from models.EmpleadoModel import EmpleadoModel
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
    if(model.FechaInicial.month != model.FechaFinal.month):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"La fecha inicial y final deben ser del mismo mes"
            }
        )
    
    traslapes = InasistenciaModel.BuscaTraslape(model)
    if(len(traslapes) > 0):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"El registro se traslapa con la inasistencia { traslapes[0]['IdInasistencia'] }"
            }
        )
    
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
    print(model)
    count = 1
    for _ in range(model.Cantidad): 
        model.Mes = count       
        PeriodoPlanillaModel.InsertarPeriodoPlanilla(model,IdUsuario)
        count = count + 1
    return

@routerPeriodoPlanilla.delete("/periodoplanilla/{Anio}/{Mes}")
async def periodoplanilla_delete(Anio:int,Mes:int):
    ret = PeriodoPlanillaModel.EliminarPeriodoPlanilla(Anio,Mes)
    return ret

#@routerPeriodoPlanilla.post("/periodoplanilla/{IdUsuario}/{IdPeriodoPlanilla}")
#async def periodoplanilla_post(IdUsuario,IdPeriodoPlanilla,model:PeriodoPlanillaRequest):
#    ret = PeriodoPlanillaModel.ActualizarPeriodoPlanilla(model,IdUsuario,IdPeriodoPlanilla)
#    print(ret)
#    return ret



# Empleado
routerEmpleado = APIRouter(
    tags=["Empleado"],
)

@routerEmpleado.get('/empleado')
async def empleado_get():
    empleado = EmpleadoModel.ObtenerTodosEmpleado()
    return empleado

@routerEmpleado.get('/empleadocontratado')
async def empleadocontratado_get():
    empleado = EmpleadoModel.ObtenerEmpleadoContratado()
    return empleado


router.include_router(routerStatusEmpleado)
router.include_router(routerInasistencia)
router.include_router(routerPeriodoPlanilla)
router.include_router(routerEmpleado)