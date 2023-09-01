from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from schemas.UsuarioSchema import LoginRequest
from models.UsuarioModel import UsuarioModel
from models.ModuloModel import ModuloModel
from models.MenuModel import MenuModel
from models.OpcionModel import OpcionModel


router = APIRouter(
    prefix="/User",
    tags=["User"],
)

@router.post('/login')
async def login(model:LoginRequest):
    ret = UsuarioModel.ComprobarCredenciales(model.IdUsuario,model.Password)
    if ret is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":"Usuario y/o contraseña no son válidos"
            }
        )
    
    
    espuesta = {
        "error":False,
        "token":"",
        "expires_at":"",
        "id_user":ret["IdUsuario"],
        "user":ret
    }
    return espuesta


@router.get('/menu/{IdUsuario}')
async def menu(IdUsuario):
    modulos = ModuloModel.ObtenerModulos(IdUsuario)
    print(modulos)
    menuAll = []

    for modulo in modulos:
        print(modulo)
        idModulo:int = int(modulo["IdModulo"])
        menus = MenuModel.ObtenerMenus(IdUsuario,idModulo)

        menuLst = []

        for menu in menus:
            idMenu = int(menu["IdMenu"])
            opciones = OpcionModel.ObtenerOpciones(IdUsuario,idModulo,idMenu)

            menus_obj = {
                "id":menu["IdMenu"],
                "nombre":menu["Menu"],
                "submenu":opciones
            }

            menuLst.append(menus_obj)

        modulos_obj = {
            "id":modulo["IdModulo"],
            "nombre":modulo["Nombre"],
            "submenu":menuLst
        }

        menuAll.append(modulos_obj)
    
    return {
        "error":False,
        "opciones":menuAll
    }



