from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/suseso/consultaAfiliacionMutual/{rut}/{dv}")
async def testsusesoconsultaAfiliacionMutual(rut: str, dv: str):
    return JSONResponse(content={
        "return": "-40",
        "transaction": "12345678",
        "Mutuales": {
            "Mutual": {"nombre": "INSTITUTO [REDACTED]"}
        },
    })
