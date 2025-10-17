from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.sleep import with_sleep

router = APIRouter()


@router.get("/suseso/consultaAfiliacionCaja/{rut}")
@with_sleep()  # You can change the delay time in milliseconds here
async def testsusesoconsultaAfiliacionCaja(rut: str):
    return JSONResponse(content={
        "cajas": [
            {
                "nombre": "18 de [REDACTED]",
                "fecha_ingreso": "2022-01-01",
                "empleador": "[REDACTED]",
                "tipo_afiliacion": "[REDACTED]",
            }
        ],
        "mensaje": None,
        "submensaje": None,
        "exitoso": True,
        "codigo": 200
    })
