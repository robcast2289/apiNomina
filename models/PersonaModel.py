from repositories.mysql.mysql_db import MySqldb

class PersonaModel:
    def InsertarPersona(data,usuario):
        params = [
            {"nombre":"Nombre","valor":data.Nombre,},            
            {"nombre":"Apellido","valor":data.Apellido,},          

            {
                "nombre":"UsuarioCreacion",
                "valor":usuario,
            }
        ]
        query = f"""
insert into persona
(
    Nombre,
    Apellido
)
values
(%s,%s,NOW(),%s)
"""
        ret = MySqldb().execute_insert(query,params=params)
        
        return ret