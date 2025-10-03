from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/spensiones/ConsultaCotizaciones/{rut}")
async def testspensionesConsultaCotizaciones(rut: str):
    json = JSONResponse(content={
        "rut": rut,
        "nombres": "Alex",
        "apellidos": "Murphy",
        "fecha_corte_afp": "2025-10-01",
        "cotizaciones": [
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2025-09",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2025-08-31",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2025-08",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2025-07-31",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2025-07",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2025-06-30",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2025-06",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2025-05-31",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2025-05",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2025-04-30",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2025-04",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2025-03-31",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2025-03",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2025-02-28",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2025-02",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2025-01-31",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2025-01",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2024-12-31",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2024-12",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2024-11-30",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2024-11",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2024-10-31",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            },
            {
                "rut_afp": "99999999-9",
                "periodo_cotizado": "2024-10",
                "monto_cotizado": 100500,
                "porcentaje_cotizacion": 10.05,
                "fecha_pago": "2024-09-30",
                "monto_remuneracion_imponible": 1000000,
                "tipo_movimiento": "Cotizaci\u00f3n",
                "fondo_destino": "A",
                "rut_pagador_empleador": "88888888-8"
            }
        ]
    })
    print("JSON to be returned:", json)
    return json
