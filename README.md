
# Instalación y Ejecución del Proyecto SPS02 FastAPI Mock

**Instalar dependencias usando uv**

```bash
uv sync
```

3. **Activar el entorno virtual**

```bash
source .venv/bin/activate
```

**Levantar el servicio**

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8008
```

# Configurar archivo CSV para sps02_etls

Copiar el archivo de ejemplo, o poblar la carpeta CSV con los archivos necesarios:

```bash
cp  DT/CSV_EXAMPLE DT/CSV
```
