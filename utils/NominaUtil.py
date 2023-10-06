from schemas.RRHHSchema import PersonaRequest
from schemas.NominaSchemas import NuevoEmpleadoRequest, EmpleadoRequest
from models.PersonaModel import PersonaModel

class NominaUtil:
    def CrearEmpleado(idusuario,model:NuevoEmpleadoRequest):
        persona = PersonaRequest(
            Nombre=model.Nombre,
            Apellido=model.Apellido,
            FechaNacimiento=model.FechaNacimiento,
            IdGenero=model.IdGenero,
            IdEstadoCivil=model.IdEstadoCivil,
            Direccion=model.Direccion,
            Telefono=model.Telefono,
            CorreoElectronioco=model.CorreoElectronioco
        )

        ret = PersonaModel.InsertarPersona(persona,idusuario)

        print(ret)

        return