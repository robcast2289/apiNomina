from repositories.mysql.mysql_db import MySqldb

class SucursalModel:
    
    def ObtenerSucursal():
        query = f"""
select 
    a.IdSucursal,
    a.Nombre,
    a.Direccion, 
    a.IdEmpresa, 
    b.Nombre Empresa
from 
    sucursal a 
    inner join empresa b on a.IdEmpresa = b.IdEmpresa
"""
        ret = MySqldb().execute_query(query)
        
        return ret