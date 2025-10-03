from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/ips/proximaFechaPagoBeneficios/{rut}")
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
