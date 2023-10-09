from fastapi import status
from fastapi.responses import JSONResponse
from schemas.RRHHSchema import PersonaRequest
from schemas.NominaSchemas import NuevoEmpleadoRequest, EditarEmpleadoRequest, EmpleadoRequest
from models.PersonaModel import PersonaModel
from models.EmpleadoModel import EmpleadoModel

class NominaUtil:
    def CrearEmpleado(idusuario,model:NuevoEmpleadoRequest):
        persona = PersonaRequest(
            IdPersona=0,
            Nombre=model.Nombre,
            Apellido=model.Apellido,
            FechaNacimiento=model.FechaNacimiento,
            IdGenero=model.IdGenero,
            IdEstadoCivil=model.IdEstadoCivil,
            Direccion=model.Direccion,
            Telefono=model.Telefono,
            CorreoElectronico=model.CorreoElectronico
        )

        try:
            ret = PersonaModel.InsertarPersona(persona,idusuario)
        except Exception as ex:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":str(ex)
                }
            )
        
        if ret is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Error al crear empleado"
                }
            )

        empleado = EmpleadoRequest(
            IdEmpleado=0,
            IdPersona=ret,
            IdSucursal=model.IdSucursal,
            FechaContratacion=model.FechaContratacion,
            IdPuesto=model.IdPuesto,
            IdStatusEmpleado=model.IdStatusEmpleado,
            IngresoSueldoBase=model.IngresoSueldoBase,
            IngresoBonificacionDecreto=model.IngresoBonificacionDecreto,
            IngresoOtrosIngresos=model.IngresoOtrosIngresos,
            DescuentoIgss=model.DescuentoIgss,
            DescuentoIsr=model.DescuentoIsr,
            DescuentoInasistencias=model.DescuentoInasistencias
        )

        try:
            retEmpl = EmpleadoModel.InsertarEmpleado(empleado,idusuario)            
        except Exception as ex:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":str(ex)
                }
            )
        print(retEmpl)
        return retEmpl
    


    def actualizarEmpleado(idusuario,model:EditarEmpleadoRequest):
        persona = PersonaRequest(
            IdPersona=model.IdPersona,
            Nombre=model.Nombre,
            Apellido=model.Apellido,
            FechaNacimiento=model.FechaNacimiento,
            IdGenero=model.IdGenero,
            IdEstadoCivil=model.IdEstadoCivil,
            Direccion=model.Direccion,
            Telefono=model.Telefono,
            CorreoElectronico=model.CorreoElectronico
        )

        try:
            ret = PersonaModel.ActualizarPersona(persona,idusuario)
        except Exception as ex:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":str(ex)
                }
            )
        
        if ret is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":"Error al actualizar empleado"
                }
            )

        empleado = EmpleadoRequest(
            IdEmpleado=model.IdEmpleado,
            IdPersona=model.IdPersona,
            IdSucursal=model.IdSucursal,
            FechaContratacion=model.FechaContratacion,
            IdPuesto=model.IdPuesto,
            IdStatusEmpleado=model.IdStatusEmpleado,
            IngresoSueldoBase=model.IngresoSueldoBase,
            IngresoBonificacionDecreto=model.IngresoBonificacionDecreto,
            IngresoOtrosIngresos=model.IngresoOtrosIngresos,
            DescuentoIgss=model.DescuentoIgss,
            DescuentoIsr=model.DescuentoIsr,
            DescuentoInasistencias=model.DescuentoInasistencias
        )

        try:
            retEmpl = EmpleadoModel.ActualizarEmpleado(empleado,idusuario)        
        except Exception as ex:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error":True,
                    "mensaje":str(ex)
                }
            )

        return retEmpl
