from fastapi import APIRouter, Depends, HTTPException, status
from models.ModuloModel import ModuloModel
from models.MenuModel import MenuModel
from models.OpcionModel import OpcionModel
from models.RoleModel import RoleModel
from models.RoleOpcionModel import RoleOpcionModel
from models.UsuarioTableModel import UsuarioTableModel
#from schemas.SeguridadSchema import ModuloRequest,MenuRequest,OpcionRequest,RoleRequest,RoleOpcionRequest
from schemas.SeguridadSchema import *

router = APIRouter(
    prefix="/seguridad",
    #tags=["Seguridad"],
)


# GENERALES

# Modulos
routerModulo = APIRouter(
    tags=["Modulos"],
)

@routerModulo.get('/generales/modulos')
async def modulos_get():
    modulos = ModuloModel.ObtenerTodosModulos()
    return modulos

@routerModulo.put("/generales/modulos/{IdUsuario}")
async def modulos_put(IdUsuario,model:ModuloRequest):
    ModuloModel.InsertarModulo(model,IdUsuario)
    return

@routerModulo.delete("/generales/modulos/{IdModulo}")
async def modulos_delete(IdModulo):
    ret = ModuloModel.EliminarModulo(IdModulo)
    return ret

@routerModulo.post("/generales/modulos/{IdUsuario}/{IdModulo}")
async def modulos_post(IdUsuario,IdModulo,model:ModuloRequest):
    ret = ModuloModel.ActualizarModulo(model,IdUsuario,IdModulo)
    print(ret)
    return ret



# Menus
routerMenu = APIRouter(
    tags=["Menus"],
)

@routerMenu.get('/generales/menus')
async def menus_get():
    menus = MenuModel.ObtenerTodosMenus()
    return menus

@routerMenu.put("/generales/menus/{IdUsuario}")
async def menus_put(IdUsuario,model:MenuRequest):
    MenuModel.InsertarMenu(model,IdUsuario)
    return

@routerMenu.delete("/generales/menus/{IdMenu}")
async def menus_delete(IdMenu):
    ret = MenuModel.EliminarMenu(IdMenu)
    return ret

@routerMenu.post("/generales/menus/{IdUsuario}/{IdMenu}")
async def menus_post(IdUsuario,IdMenu,model:MenuRequest):
    ret = MenuModel.ActualizarMenu(model,IdUsuario,IdMenu)
    return ret


# Opciones
routerOpcion = APIRouter(
    tags=["Opciones"],
)

@routerOpcion.get('/generales/opciones')
async def opciones_get():
    opciones = OpcionModel.ObtenerTodosOpciones()
    return opciones

@routerOpcion.get('/generales/opciones/buscaruta/{IdUsuario}/{ruta}')
async def opciones_ruta_get(IdUsuario,ruta):
    print(IdUsuario)
    print(ruta)
    if(ruta == 'home'):
        return True
    opcionBuscado = OpcionModel.findOpcionByRoute(ruta)[0]
    acceso = OpcionModel.tieneAcceso(IdUsuario,opcionBuscado["IdOpcion"])
    return acceso

@routerOpcion.put("/generales/opciones/{IdUsuario}")
async def opciones_put(IdUsuario,model:OpcionRequest):
    OpcionModel.InsertarOpcion(model,IdUsuario)
    return

@routerOpcion.delete("/generales/opciones/{IdOpcion}")
async def opciones_delete(IdOpcion):
    ret = OpcionModel.EliminarOpcion(IdOpcion)
    return ret

@routerOpcion.post("/generales/opciones/{IdUsuario}/{IdOpcion}")
async def opciones_post(IdUsuario,IdOpcion,model:OpcionRequest):
    ret = OpcionModel.ActualizarOpcion(model,IdUsuario,IdOpcion)
    return ret


# Roles
routerRole = APIRouter(
    tags=["Roles"],
)

@routerRole.get('/generales/roles/{IdRole}')
async def roles_get(IdRole):
    roles = RoleModel.ObtenerUnicoRole(IdRole)
    return roles[0]

@routerRole.get('/generales/roles')
async def roles_get():
    roles = RoleModel.ObtenerTodosRoles()
    return roles

@routerRole.put("/generales/roles/{IdUsuario}")
async def roles_put(IdUsuario,model:RoleRequest):
    RoleModel.InsertarRole(model,IdUsuario)
    return

@routerRole.delete("/generales/roles/{IdRole}")
async def roles_delete(IdRole):
    ret = RoleModel.EliminarRole(IdRole)
    return ret

@routerRole.post("/generales/roles/{IdUsuario}/{IdRole}")
async def roles_post(IdUsuario,IdRole,model:RoleRequest):
    ret = RoleModel.ActualizarRole(model,IdUsuario,IdRole)
    return ret


# Role-Opciones
routerRoleOpcion = APIRouter(
    tags=["RoleOpciones"],
)

@routerRoleOpcion.get('/generales/rolesopcion/{IdRole}')
async def roles_get(IdRole):
    rolesopcion = RoleOpcionModel.ObtenerTodosRoleOpcion(IdRole)
    return rolesopcion

@routerRoleOpcion.put("/generales/rolesopcion/{IdUsuario}")
async def rolesopcion_put(IdUsuario,model:RoleOpcionRequest):
    RoleOpcionModel.InsertarRoleOpcion(model,IdUsuario)
    return

@routerRoleOpcion.delete("/generales/rolesopcion/{IdRole}/{IdOpcion}")
async def rolesopcion_delete(IdRole,IdOpcion):
    ret = RoleOpcionModel.EliminarRoleOpcion(IdRole,IdOpcion)
    return ret

@routerRoleOpcion.post("/generales/rolesopcion/{IdUsuario}/{IdRole}/{IdOpcion}")
async def rolesopcion_post(IdUsuario,IdRole,IdOpcion,model:RoleOpcionRequest):
    ret = RoleOpcionModel.ActualizarRoleOpcion(model,IdUsuario,IdRole,IdOpcion)
    return ret


# Usuarios
routerUsuario = APIRouter(
    tags=["Usuarios"],
)

@routerUsuario.get('/generales/usuarios/{IdUsuario}')
async def usuarios_get(IdUsuarioTable):
    usuarios = UsuarioTableModel.ObtenerUnicoUsuarios(IdUsuarioTable)
    return usuarios[0]

@routerUsuario.get('/generales/usuarios')
async def usuarios_get():
    usuarios = UsuarioTableModel.ObtenerTodosUsuarios()
    return usuarios

@routerUsuario.put("/generales/usuarios/{IdUsuario}")
async def usuarios_put(IdUsuario,model:UsuarioRequest):
    UsuarioTableModel.InsertarUsuarios(model,IdUsuario)
    return

@routerUsuario.delete("/generales/usuarios/{IdUsuarioTable}")
async def usuarios_delete(IdUsuarioTable):
    ret = UsuarioTableModel.EliminarUsuarios(IdUsuarioTable)
    return ret

@routerUsuario.post("/generales/usuarios/{IdUsuario}/{IdUsuarioTable}")
async def usuarios_post(IdUsuario,IdUsuarioTable,model:UsuarioRequest):
    ret = UsuarioTableModel.ActualizarUsuarios(model,IdUsuario,IdUsuarioTable)
    return ret


router.include_router(routerModulo)
router.include_router(routerMenu)
router.include_router(routerOpcion)
router.include_router(routerRole)
router.include_router(routerRoleOpcion)
router.include_router(routerUsuario)