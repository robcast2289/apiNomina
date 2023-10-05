from repositories.mysql.mysql_db import MySqldb

class EmpleadoModel:
    def ObtenerTodosEmpleado():
        query = f"""
select 
    a.IdEmpleado,
    b.Nombre,
    b.Apellido,
    a.FechaContratacion,
    c.Nombre Status
from 
    empleado a,
    persona b,
    status_empleado c
where 
    a.IdPersona = b.IdPersona
    and a.IdStatusEmpleado = c.IdStatusEmpleado
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    
    def ObtenerEmpleadoContratado():
        query = f"""
select 
    a.IdEmpleado,
    b.Nombre,
    b.Apellido,
    c.Nombre Status
from 
    empleado a,
    persona b,
    status_empleado c
where 
    a.IdPersona = b.IdPersona
    and a.IdStatusEmpleado = c.IdStatusEmpleado
    and c.IdStatusEmpleado in (1,2,3)
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def ObtenerEmpleadoActivo():
        query = f"""
select 
    a.IdEmpleado,
    b.Nombre,
    b.Apellido,
    c.Nombre Status
from 
    empleado a,
    persona b,
    status_empleado c
where 
    a.IdPersona = b.IdPersona
    and a.IdStatusEmpleado = c.IdStatusEmpleado
    and c.IdStatusEmpleado = 1
"""
        ret = MySqldb().execute_query(query)
        
        return ret
    

    def InsertarEmpleado(data,usuario):
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