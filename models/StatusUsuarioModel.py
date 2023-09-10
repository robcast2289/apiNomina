from repositories.mysql.mysql_db import MySqldb

class StatusUsuarioModel:
    
    def ObtenerStatusUsuario():
        query = f"""
select 
    a.IdStatusUsuario,
    a.Nombre 
from 
    status_usuario a 
"""
        ret = MySqldb().execute_query(query)
        
        return ret