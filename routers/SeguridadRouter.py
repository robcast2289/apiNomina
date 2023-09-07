from fastapi import APIRouter, Depends, HTTPException, status
from models.ModuloModel import ModuloModel
from models.MenuModel import MenuModel
from models.OpcionModel import OpcionModel
from models.RoleModel import RoleModel
from models.RoleOpcionModel import RoleOpcionModel
#from schemas.SeguridadSchema import ModuloRequest,MenuRequest,OpcionRequest,RoleRequest,RoleOpcionRequest
from schemas.SeguridadSchema import *

router = APIRouter(
    prefix="/seguridad",
    tags=["Seguridad"],
)

# GENERALES

# Modulos
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
    return ret

@router.post("/generales/modulos/{IdUsuario}/{IdModulo}")
async def modulos_post(IdUsuario,IdModulo,model:ModuloRequest):
    ret = ModuloModel.ActualizarModulo(model,IdUsuario,IdModulo)
    print(ret)
    return ret



# Menus
@router.get('/generales/menus')
async def menus_get():
    menus = MenuModel.ObtenerTodosMenus()
    return menus

@router.put("/generales/menus/{IdUsuario}")
async def menus_put(IdUsuario,model:MenuRequest):
    MenuModel.InsertarMenu(model,IdUsuario)
    return

@router.delete("/generales/menus/{IdMenu}")
async def menus_delete(IdMenu):
    ret = MenuModel.EliminarMenu(IdMenu)
    return ret

@router.post("/generales/menus/{IdUsuario}/{IdMenu}")
async def menus_post(IdUsuario,IdMenu,model:MenuRequest):
    ret = MenuModel.ActualizarMenu(model,IdUsuario,IdMenu)
    return ret


# Opciones
@router.get('/generales/opciones')
async def opciones_get():
    opciones = OpcionModel.ObtenerTodosOpciones()
    return opciones

@router.put("/generales/opciones/{IdUsuario}")
async def opciones_put(IdUsuario,model:OpcionRequest):
    OpcionModel.InsertarOpcion(model,IdUsuario)
    return

@router.delete("/generales/opciones/{IdOpcion}")
async def opciones_delete(IdOpcion):
    ret = OpcionModel.EliminarOpcion(IdOpcion)
    return ret

@router.post("/generales/opciones/{IdUsuario}/{IdOpcion}")
async def opciones_post(IdUsuario,IdOpcion,model:OpcionRequest):
    ret = OpcionModel.ActualizarOpcion(model,IdUsuario,IdOpcion)
    return ret


# Roles
@router.get('/generales/roles/{IdRole}')
async def roles_get(IdRole):
    roles = RoleModel.ObtenerUnicoRole(IdRole)
    return roles[0]

@router.get('/generales/roles')
async def roles_get():
    roles = RoleModel.ObtenerTodosRoles()
    return roles

@router.put("/generales/roles/{IdUsuario}")
async def roles_put(IdUsuario,model:RoleRequest):
    RoleModel.InsertarRole(model,IdUsuario)
    return

@router.delete("/generales/roles/{IdRole}")
async def roles_delete(IdRole):
    ret = RoleModel.EliminarRole(IdRole)
    return ret

@router.post("/generales/roles/{IdUsuario}/{IdRole}")
async def roles_post(IdUsuario,IdRole,model:RoleRequest):
    ret = RoleModel.ActualizarRole(model,IdUsuario,IdRole)
    return ret


# Role-Opciones
@router.get('/generales/rolesopcion/{IdRole}')
async def roles_get(IdRole):
    rolesopcion = RoleOpcionModel.ObtenerTodosRoleOpcion(IdRole)
    return rolesopcion

@router.put("/generales/rolesopcion/{IdUsuario}")
async def rolesopcion_put(IdUsuario,model:RoleOpcionRequest):
    RoleOpcionModel.InsertarRoleOpcion(model,IdUsuario)
    return

@router.delete("/generales/rolesopcion/{IdRole}/{IdOpcion}")
async def rolesopcion_delete(IdRole,IdOpcion):
    ret = RoleOpcionModel.EliminarRoleOpcion(IdRole,IdOpcion)
    return ret

@router.post("/generales/rolesopcion/{IdUsuario}/{IdRole}/{IdOpcion}")
async def rolesopcion_post(IdUsuario,IdRole,IdOpcion,model:RoleOpcionRequest):
    ret = RoleOpcionModel.ActualizarRoleOpcion(model,IdUsuario,IdRole,IdOpcion)
    return ret