from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.sleep import with_sleep

router = APIRouter()


@router.get("/ips/proximaFechaPagoBeneficios/{rut}")
@with_sleep()  # You can change the delay time in milliseconds here
async def testipsproximaFechaPagoBeneficios(rut: str):
    return JSONResponse(content={
        "glosaRetorno": "Servicio ejecutado correctamente.",
        "resultado": {
            "dvBeneficiario": "9",
            "runBeneficiario": 12345678,
            "liquidacion": {
                "proximoPago": {
                    "beneficio": "SUBSIDIO [REDACTED]",
                    "descripcionBeneficio": "[REDACTED]",
                    "formaPago": "[REDACTED]",
                    "fechaProxPago": "[REDACTED]"
                }
            }
        },
        "codigoRetorno": "0",
        "timestamp": 12345678
    })
