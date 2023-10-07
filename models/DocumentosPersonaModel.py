from repositories.mysql.mysql_db import MySqldb

class DocumentosPersonaModel:
    def ObtenerTodosDocumentosPersona(idpersona):
        query = f"""
select 
    a.IdTipoDocumento,
    b.Nombre TipoDocumento,
    a.IdPersona,
    a.NoDocumento 
from 
    documento_persona a, 
    tipo_documento b 
where 
    a.IdTipoDocumento = b.IdTipoDocumento
    and a.IdPersona = {idpersona} 
"""
        ret = MySqldb().execute_query(query)
        
        return ret