from repositories.mysql.mysql_db import MySqldb

class MenuModel:
    
    def ObtenerMenus(usr:str,modulo:int):
        query = f"""
select 
    b.IdMenu,
    b.Nombre Menu
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
group by a.IdModulo, a.Nombre, b.IdMenu,b.Nombre
order by b.OrdenMenu asc
"""
        ret = MySqldb().execute_query(query)
        
        return ret