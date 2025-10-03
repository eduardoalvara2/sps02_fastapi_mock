from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.routers import ipsproximaFechaPagoBeneficios, ipsobtenerresolucionAF
from app.routers import susesoconsultaAfiliacionCaja, susesoconsultaAfiliacionMutual
from app.routers import susesoSIAGFConsultaCausanteSimple, spensionesConsultaCotizaciones

app = FastAPI()

@app.get("/healthz")
async def health_check():
    return {"ok": True}


app.include_router(ipsproximaFechaPagoBeneficios.router)
app.include_router(ipsobtenerresolucionAF.router)
app.include_router(susesoconsultaAfiliacionCaja.router)
app.include_router(susesoconsultaAfiliacionMutual.router)
app.include_router(susesoSIAGFConsultaCausanteSimple.router)
app.include_router(spensionesConsultaCotizaciones.router)
