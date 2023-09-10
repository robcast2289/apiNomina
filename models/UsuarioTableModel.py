from repositories.mysql.mysql_db import MySqldb

class UsuarioTableModel:
    
    def ObtenerTodosUsuarios():
            query = f"""
    select 
        a.IdUsuario,
        a.Nombre,
        a.Apellido,
        a.FechaNacimiento,
        a.IdStatusUsuario,
        b.Nombre Status,
        a.IdGenero,
        c.Nombre Genero,
        a.UltimaFechaIngreso,
        a.IntentosDeAcceso,
        a.SesionActual,
        a.UltimaFechaCambioPassword,
        a.CorreoElectronico,
        a.RequiereCambiarPassword,
        a.Fotografia,
        a.TelefonoMovil,
        a.IdSucursal,
        d.Nombre Sucursal
    from 
        usuario a,
        status_usuario b, 
        genero c, 
        sucursal d 
    where
        a.IdStatusUsuario = b.IdStatusUsuario
        and a.IdGenero = c.IdGenero
        and a.IdSucursal = d.IdSucursal
    """
            ret = MySqldb().execute_query(query)
            
            return ret
    
    def ObtenerUnicoUsuarios(id):
            query = f"""
    select 
        a.IdUsuario,
        a.Nombre,
        a.Apellido,
        a.FechaNacimiento,
        a.IdStatusUsuario,
        a.IdGenero,
        a.UltimaFechaIngreso,
        a.IntentosDeAcceso,
        a.SesionActual,
        a.UltimaFechaCambioPassword,
        a.CorreoElectronico,
        a.RequiereCambiarPassword,
        a.Fotografia,
        a.TelefonoMovil,
        a.IdSucursal
    from 
        usuario a
    where
        a.IdUsuario = '{id}'
    """
            ret = MySqldb().execute_query(query)
            
            return ret
    
    def EliminarUsuarios(id:int):
        query = f"""
delete
from usuario
where IdUsuario = '{id}'
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def InsertarUsuarios(data,usuario):

        params = [
            {"nombre":"IdUsuario","valor":data.UsuarioNuevo,},
            {"nombre":"Nombre","valor":data.Nombre,},
            {"nombre":"Apellido","valor":data.Apellido,},
            {"nombre":"FechaNacimiento","valor":data.FechaNacimiento,},
            {"nombre":"IdStatusUsuario","valor":data.IdStatusUsuario,},
            {"nombre":"IdGenero","valor":data.IdGenero,},
            {"nombre":"CorreoElectronico","valor":data.CorreoElectronico,},
            #{"nombre":"Fotografia","valor":data.Fotografia,},
            {"nombre":"TelefonoMovil","valor":data.TelefonoMovil,},
            {"nombre":"IdSucursal","valor":data.IdSucursal,},
            {"nombre":"Passwrod","valor":data.Password,},
            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into usuario
(
IdUsuario,
Nombre,
Apellido,
FechaNacimiento,
IdStatusUsuario,
IdGenero,
CorreoElectronico,

TelefonoMovil,
IdSucursal,
Password,
FechaCreacion,UsuarioCreacion)
values
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret
    

    def ActualizarUsuarios(data,usuario,id):

        params = [
            {"nombre":"Nombre","valor":data.Nombre,},
            {"nombre":"Apellido","valor":data.Apellido,},
            {"nombre":"FechaNacimiento","valor":data.FechaNacimiento,},
            {"nombre":"IdStatusUsuario","valor":data.IdStatusUsuario,},
            {"nombre":"IdGenero","valor":data.IdGenero,},
            {"nombre":"UltimaFechaIngreso","valor":data.UltimaFechaIngreso,},
            {"nombre":"IntentosDeAcceso","valor":data.IntentosDeAcceso,},
            {"nombre":"SesionActual","valor":data.SesionActual,},
            {"nombre":"UltimaFechaCambioPassword","valor":data.UltimaFechaCambioPassword,},
            {"nombre":"CorreoElectronico","valor":data.CorreoElectronico,},
            {"nombre":"RequiereCambiarPassword","valor":data.RequiereCambiarPassword,},
            {"nombre":"Fotografia","valor":data.Fotografia,},
            {"nombre":"TelefonoMovil","valor":data.TelefonoMovil,},
            {"nombre":"IdSucursal","valor":data.IdSucursal,},

            {"nombre":"UsuarioModificacion","valor":usuario,},
            {"nombre":"IdUsuario","valor":id,}            
        ]
        query = f"""
update role 
set 
Nombre=%s, 
Apellido=%s, 
FechaNacimiento=%s, 
IdStatusUsuario=%s, 
IdGenero=%s, 
UltimaFechaIngreso=%s, 
IntentosDeAcceso=%s, 
SesionActual=%s, 
UltimaFechaCambioPassword=%s, 
CorreoElectronico=%s, 
RequiereCambiarPassword=%s, 
Fotografia=%s, 
TelefonoMovil=%s, 
IdSucursal=%s  
FechaModificacion=NOW(), 
UsuarioModificacion=%s
where IdUsuario=%s
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret