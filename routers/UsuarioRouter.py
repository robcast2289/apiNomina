from fastapi import APIRouter, Depends, HTTPException, status, Request, WebSocket
from fastapi.responses import JSONResponse
import json
from schemas.UsuarioSchema import LoginRequest
from models.UsuarioModel import UsuarioModel
from models.ModuloModel import ModuloModel
from models.MenuModel import MenuModel
from models.OpcionModel import OpcionModel
from models.EmpresaModel import EmpresaModel
from models.UsuarioPreguntaModel import UsuarioPreguntaModel


router = APIRouter(
    prefix="/User",
    tags=["User"],
)

@router.post('/login')
async def login(request:Request):
    try:
        userAgent = request.headers.get("User-Agent")
        #userAgent = websocket.headers.get("User-Agent")
        #ip = f"{request.client.host}:{request.client.port}"    
        #ip = request.headers.get("Origin")
        ip = request.headers.get("X-Forwarded-For", "").split(",")[0]
        #ip = websocket.client.host

        form = await request.form()

        data = form.get("data")
        log = form.get('log')
        print(log)
        dataObject = json.loads(data)
        logObject = json.loads(log)

        model:LoginRequest = LoginRequest(
            IdUsuario=dataObject["IdUsuario"],
            Password=dataObject["Password"]
        )      
        print(model)
        ret = UsuarioModel.BuscarUsuario(model.IdUsuario)    
        if ret is None:
            ret2=UsuarioModel.InsertaBitacora(model.IdUsuario,4,userAgent,ip,"",logObject["os"],logObject["device"],logObject["browser"])
            print(ret2)
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Usuario y/o contraseña no son válidos"
                }
            )
        
        if ret["IdStatusUsuario"] != 1:
            UsuarioModel.InsertaBitacora(model.IdUsuario,ret["IdStatusUsuario"],userAgent,ip,"",logObject["os"],logObject["device"],logObject["browser"])
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":f"Usuario {ret['Status']}"
                }
            )
        
        empresa = EmpresaModel.ObtenerEmpresaUsuario(model.IdUsuario)[0]
        if ret["Password"] != model.Password:
            # CAMBIAR POR LA CANTIDAD CONFIGURADA DE INTENTOS
            if ret["IntentosDeAcceso"] < (int(empresa["PasswordIntentosAntesDeBloquear"])-1):
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

        UsuarioModel.InsertaBitacora(model.IdUsuario,1,userAgent,ip,"",logObject["os"],logObject["device"],logObject["browser"])
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


@router.post("/recover")
async def recover(request:Request):
    form = await request.form()

    data = form.get("data")
    print(data)
    dataObject = json.loads(data)

    model:LoginRequest = LoginRequest(
        IdUsuario=dataObject["IdUsuario"],
        Password=""
    )

    ret = UsuarioModel.BuscarUsuario(model.IdUsuario)    
    if ret is None:        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":"El usuario proporcionado no existe en nuestra base de datos"
            }
        )
    
    if ret["IdStatusUsuario"] != 1:        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"Usuario {ret['Status']}"
            }
        )
    
    empresa = EmpresaModel.ObtenerEmpresaUsuario(model.IdUsuario)[0]
    preguntas = UsuarioPreguntaModel.ObtenerTodosUsuarioPregunta(model.IdUsuario,int(empresa['PasswordCantidadPreguntasValidar']))
    if preguntas is None or len(preguntas) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error":True,
                "mensaje":f"El usuario proporcionado no tiene metodos de recuperación. Consulte con el administrador del sistema"
            }
        )
    
    return preguntas


@router.post('/valida_pregunta')
async def valida_pregunta(request: Request):
    form = await request.form()

    data = form.get("data")
    dataObject = json.loads(data)
    
    model:LoginRequest = LoginRequest(
        IdUsuario=dataObject["IdUsuario"],
        Password=""
    )

    quest = form.get("question")
    questObject = json.loads(quest)

    for numTest in questObject:
        idpregunta = str(numTest).replace("pregunta","")
        respuesta = UsuarioPreguntaModel.obtenerRespuesta(model.IdUsuario,int(idpregunta))
        respuestaBase = respuesta[0]["Respuesta"].upper()
        respuestaUser = str(questObject[numTest]).upper()
        print(respuestaBase)
        print(respuestaUser)


