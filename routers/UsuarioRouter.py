from fastapi import APIRouter, Depends, HTTPException, status, Request, WebSocket
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
async def login(model:LoginRequest, request:Request, websocket:WebSocket):
    try:
        userAgent = ""
        ip = ""
        userAgent = request.headers.get("User-Agent")
        #ip = f"{request.client.host}:{request.client.port}"    
        #ip = request.headers.get("Origin")
        #ip = request.headers.get("X-Forwarded-For", "").split(",")[0]
        ip = websocket.client.host
        
        print(ip)
        ret = UsuarioModel.BuscarUsuario(model.IdUsuario)    
        if ret is None:
            ret2=UsuarioModel.InsertaBitacora(model.IdUsuario,4,userAgent,ip,"","","","")
            print(ret2)
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Usuario y/o contraseña no son válidos"
                }
            )
        
        if ret["IdStatusUsuario"] != 1:
            UsuarioModel.InsertaBitacora(model.IdUsuario,ret["IdStatusUsuario"],userAgent,ip,"","","","")
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":f"Usuario {ret['Status']}"
                }
            )
        
        if ret["Password"] != model.Password:
            # CAMBIAR POR LA CANTIDAD CONFIGURADA DE INTENTOS
            if ret["IntentosDeAcceso"] < (3-1):
                UsuarioModel.ActualizaIntentoSesion(model.IdUsuario)
            else:
                UsuarioModel.ActualizaIntentoSesion(model.IdUsuario)
                UsuarioModel.BloquearUsuario(model.IdUsuario)
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Usuario y/o contraseña no son válidos"
                }
            )

        if ret["IntentosDeAcceso"] != 0:
            UsuarioModel.ReiniciaIntentoSesion(model.IdUsuario)

        UsuarioModel.InsertaBitacora(model.IdUsuario,1,userAgent,ip,"","","","")
        UsuarioModel.ActualizaUltimaSesion(model.IdUsuario)
        
        respuesta = {
            "error":False,
            "token":"",
            "expires_at":"",
            "id_user":ret["IdUsuario"],
            "user":ret
        }
        return respuesta
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":e
            }
        )


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



