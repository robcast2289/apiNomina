from repositories.mysql.mysql_db import MySqldb

class OpcionModel:
    
    def ObtenerOpciones(usr:str,modulo:int,menu:int):
        query = f"""
select 
    c.IdOpcion,
    c.Nombre Opcion,
    c.Pagina Ruta
from 
    modulo a 
    inner join menu b on a.IdModulo = b.IdModulo 
    inner join opcion c on b.IdMenu = c.IdMenu 
    inner join role_opcion ro on c.IdOpcion = ro.IdOpcion 
    inner join role r on ro.IdRole = r.IdRole 
    inner join usuario_role ur on r.IdRole = ur.IdRole 
where 
    ur.IdUsuario = '{usr}' 
    and b.IdModulo = {modulo}
    and c.IdMenu = {menu}
group by a.IdModulo, a.Nombre, b.IdMenu,b.Nombre,c.IdOpcion,c.Nombre,c.Pagina 
order by c.OrdenMenu asc
"""
        ret = MySqldb().execute_query(query)
        
        return ret