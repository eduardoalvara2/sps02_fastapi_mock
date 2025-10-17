from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.sleep import with_sleep

router = APIRouter()


@router.get("/suseso/SIAGFConsultaCausanteSimple/{rut}")
@with_sleep()  # You can change the delay time in milliseconds here
async def testsusesoSIAGFConsultaCausanteSimple(rut: str):
    return JSONResponse(content={
        "status": 200,
        "message": "OK",
        "data": {
            "FechaEmision": "2025-01-01",
            "Tuplas": [
                {
                    "EstadoTupla": {"NomEstadoTupla": "RECONOCIMIENTO VIGENTE"},
                    "Causante": {
                        "RutCausante": "1234568-9",
                        "NomCausante": "[REDACTED]",
                        "SexoCausante": "Masculino",
                        "FecNacCausante": "2005-01-01",
                        "TipoCausante": {
                            "CodTipoCausante": 1234,
                            "NomTipoCausante": "[REDACTED]",
                        },
                        "RegionCausante": {"CodRegion": 13, "NomRegion": "REGIÓN METROPOLITANA DE SANTIAGO"},
                        "ComunaCausante": {"CodComuna": 13118, "NomComuna": "MACUL"},
                    },
                    "FechaTransaccion": "2025-01-01",
                    "Beneficiario": {
                        "RutBeneficiario": "1234568-9",
                        "NomBeneficiario": "[REDACTED]",
                        "TipoBeneficiario": {"CodTipoBeneficiario": 1234, "NomTipoBeneficiario": "[REDACTED]"},
                        "IngPromedio": 123456,
                        "Empleador": {
                            "RutEmpleador": "12345678-9",
                            "NomEmpleador": "[REDACTED]",
                            "Acteco": 123456,
                            "RegionEmpleador": {"CodRegion": 13, "NomRegion": "REGIÓN METROPOLITANA DE SANTIAGO"},
                            "ComunaEmpleador": {"CodComuna": 13113, "NomComuna": "LA REINA"},
                        },
                    },
                    "EntidadAdm": {
                        "CodEntidadAdm": 1234,
                        "NomEntidadAdm": "[REDACTED]",
                        "Beneficio": {
                            "CodTipoBeneficio": 1234,
                            "NomTipoBeneficio": "[REDACTED]",
                            "FecRecCausante": "2025-01-01",
                            "FecPagoBeneficio": "2025-01-01",
                            "PuntajeFichaProtSocial": None,
                            "MontoUnitarioBeneficio": 1234,
                            "TramoAsigFam": 1234,
                        },
                    },
                },
                {
                    "EstadoTupla": {"NomEstadoTupla": "RECONOCIMIENTO VIGENTE"},
                    "Causante": {
                        "RutCausante": "1234568-9",
                        "NomCausante": "[REDACTED]",
                        "SexoCausante": "Femenino",
                        "FecNacCausante": "2005-01-01",
                        "TipoCausante": {
                            "CodTipoCausante": 1234,
                            "NomTipoCausante": "[REDACTED]",
                        },
                        "RegionCausante": {"CodRegion": 13, "NomRegion": "REGIÓN METROPOLITANA DE SANTIAGO"},
                        "ComunaCausante": {"CodComuna": 13118, "NomComuna": "MACUL"},
                    },
                    "FechaTransaccion": "2025-01-01",
                    "Beneficiario": {
                        "RutBeneficiario": "1234568-9",
                        "NomBeneficiario": "[REDACTED]",
                        "TipoBeneficiario": {"CodTipoBeneficiario": 1234, "NomTipoBeneficiario": "[REDACTED]"},
                        "IngPromedio": 123456,
                        "Empleador": {
                            "RutEmpleador": "12345678-9",
                            "NomEmpleador": "[REDACTED]",
                            "Acteco": 123456,
                            "RegionEmpleador": {"CodRegion": 13, "NomRegion": "REGIÓN METROPOLITANA DE SANTIAGO"},
                            "ComunaEmpleador": {"CodComuna": 13113, "NomComuna": "LA REINA"},
                        },
                    },
                    "EntidadAdm": {
                        "CodEntidadAdm": 1234,
                        "NomEntidadAdm": "[REDACTED]",
                        "Beneficio": {
                            "CodTipoBeneficio": 1234,
                            "NomTipoBeneficio": "[REDACTED]",
                            "FecRecCausante": "2025-01-01",
                            "FecPagoBeneficio": "2025-01-01",
                            "PuntajeFichaProtSocial": None,
                            "MontoUnitarioBeneficio": 1234,
                            "TramoAsigFam": 1234,
                        },
                    },
                },

            ],
        },
    })
