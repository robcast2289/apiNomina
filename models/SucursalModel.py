from repositories.mysql.mysql_db import MySqldb

class SucursalModel:
    
    def ObtenerSucursal():
        query = f"""
select 
    a.IdSucursal,
    a.Nombre 
from 
    sucursal a 
"""
        ret = MySqldb().execute_query(query)
        
        return ret