
# Instalación y Ejecución del Proyecto SPS02 FastAPI Mock

**Instalar dependencias usando uv**

```bash
# 1) Instalar
uv venv

# 2) Activar venv (uv gestiona todo)
source .venv/bin/activate

# 3) Sincronizar el entorno
uv sync
```

# Configuraciones para desarrollo sps02_fastapi_connector:

Para IPS, SUSESO, y SUBPREVS, levantar el servicio:

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8008
```

Para la DT, crear la BDD y las tablas:

```bash
mysql -u root -p <  sps02_fastapi_mock.sql
```

# Configurar para sps02_etls

**
Copiar el archivo de ejemplo, o poblar la carpeta CSV con los archivos necesarios:

```bash
cp  DT/CSV_EXAMPLE DT/CSV
```


