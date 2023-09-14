from repositories.mysql.mysql_db import MySqldb
from utils.Cipher import vigenere_cipher
class UsuarioModel:
    # YA NO SE USA
    def ComprobarCredenciales(usr:str, pwd:str):
        #new_pwd = vigenere_cipher(pwd,"analisisdesistemas")
        new_pwd = pwd
        print(new_pwd)
        query = f"select * from usuario where IdUsuario = '{usr}' and Password = '{new_pwd}'"
        ret = MySqldb().execute_query(query)
        try:
            Usuario = ret[0]
            return Usuario
        except Exception:
            return None
        

    def BuscarUsuario(usr:str):
        query = f"""
select 
    a.*,
    b.Nombre Status
from usuario a,
status_usuario b 
where a.IdStatusUsuario = b.IdStatusUsuario 
and a.IdUsuario = '{usr}'"""
        ret = MySqldb().execute_query(query)
        try:
            Usuario = ret[0]
            return Usuario
        except Exception:
            return None
        

    def ActualizaUltimaSesion(usr:str):
        params = [
            {"nombre":"UsuarioModificacion","valor":usr,},
            {"nombre":"IdUsuario","valor":usr,}            
        ]
        query = f"""
update usuario 
set 
UltimaFechaIngreso=NOW(), 
FechaModificacion=NOW(), 
UsuarioModificacion=%s 
where IdUsuario=%s 
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
    

    def ActualizaIntentoSesion(usr:str):
        params = [
            {"nombre":"UsuarioModificacion","valor":usr,},
            {"nombre":"IdUsuario","valor":usr,}            
        ]
        query = f"""
update usuario 
set 
IntentosDeAcceso=IntentosDeAcceso+1, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s 
where IdUsuario=%s 
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
    

    def ReiniciaIntentoSesion(usr:str):
        params = [
            {"nombre":"UsuarioModificacion","valor":usr,},
            {"nombre":"IdUsuario","valor":usr,}            
        ]
        query = f"""
update usuario 
set 
IntentosDeAcceso=0, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s 
where IdUsuario=%s 
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
    

    def BloquearUsuario(usr:str):
        params = [
            {"nombre":"UsuarioModificacion","valor":usr,},
            {"nombre":"IdUsuario","valor":usr,}            
        ]
        query = f"""
update usuario 
set 
IdStatusUsuario=2, 
FechaModificacion=NOW(), 
UsuarioModificacion=%s 
where IdUsuario=%s 
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret

    
    def InsertaBitacora(usuario,tipo_acceso):
        params = [
            {"nombre":"IdUsuario","valor":usuario,},            
            {"nombre":"IdTipoAcceso","valor":tipo_acceso,}
        ]
        query = f"""
insert into bitacora_acceso 
(
IdUsuario,
IdTipoAcceso,
FechaAcceso
) 
values 
(%s,%s,NOW())
"""
        ret = MySqldb().execute_insert(query,params=params)        
        return ret
        
    