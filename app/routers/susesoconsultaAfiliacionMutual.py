from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.sleep import with_sleep

router = APIRouter()


@router.get("/suseso/consultaAfiliacionMutual/{rut}/{dv}")
@with_sleep(100)  # You can change the delay time in milliseconds here
async def testsusesoconsultaAfiliacionMutual(rut: str, dv: str):
    return JSONResponse(content={
        "return": "-40",
        "transaction": "12345678",
        "Mutuales": {
            "Mutual": {"nombre": "INSTITUTO [REDACTED]"}
        }
    })
