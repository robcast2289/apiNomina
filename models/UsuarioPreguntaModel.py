from repositories.mysql.mysql_db import MySqldb

class UsuarioPreguntaModel:
    def ObtenerTodosUsuarioPregunta(idusuario):
        query = f"""
    select 
        a.IdPregunta,
        a.IdUsuario,
        a.Pregunta,
        a.Respuesta
    from 
        usuario_pregunta a
    where 
        a.IdUsuario = '{idusuario}'
    """
        ret = MySqldb().execute_query(query)            
        return ret