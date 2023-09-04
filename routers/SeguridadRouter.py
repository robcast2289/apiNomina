from fastapi import APIRouter, Depends, HTTPException, status
from models.ModuloModel import ModuloModel
from schemas.SeguridadSchema import ModuloRequest


router = APIRouter(
    prefix="/seguridad",
    tags=["Seguridad"],
)

@router.get('/generales/modulos')
async def modulos_get():
    modulos = ModuloModel.ObtenerTodosModulos()
    return modulos

@router.put("/generales/modulos/{IdUsuario}")
async def modulos_put(IdUsuario,model:ModuloRequest):
    ModuloModel.InsertarModulo(model,IdUsuario)
    return

@router.delete("/generales/modulos/{IdModulo}")
async def modulos_delete(IdModulo):
    ret = ModuloModel.EliminarModulo(IdModulo)
    print(ret)
    return ret