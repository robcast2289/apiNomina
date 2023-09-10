from repositories.mysql.mysql_db import MySqldb

class GeneroModel:
    
    def ObtenerGenero():
        query = f"""
select 
    a.IdGenero,
    a.Nombre 
from 
    genero a 
"""
        ret = MySqldb().execute_query(query)
        
        return ret