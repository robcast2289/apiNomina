from repositories.mysql.mysql_db import MySqldb

class ModuloModel:
    
    def ObtenerModulos(usr:str):
        query = f"""
select 
    a.IdModulo,
    a.Nombre 
from 
    modulo a 
    inner join menu b on a.IdModulo = b.IdModulo 
    inner join opcion c on b.IdMenu = c.IdMenu 
    inner join role_opcion ro on c.IdOpcion = ro.IdOpcion 
    inner join role r on ro.IdRole = r.IdRole 
    inner join usuario_role ur on r.IdRole = ur.IdRole 
where ur.IdUsuario = '{usr}' 
group by a.IdModulo, a.Nombre
"""
        ret = MySqldb().execute_query(query)
        
        return ret
        