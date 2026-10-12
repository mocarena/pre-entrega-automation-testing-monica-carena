
import csv
import json
from pathlib import Path

# Raíz del proyecto
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
CARPETA_DATOS = RAIZ_PROYECTO / "datos"


def leer_csv_login(ruta_archivo=None):
    """Lee los casos de login desde un archivo CSV."""
    if ruta_archivo is None:
        ruta_archivo = CARPETA_DATOS / "login.csv"

    with open(ruta_archivo, mode="r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        casos = []

        for fila in lector:
            debe_funcionar = fila["debe_funcionar"].strip().lower() in (
                "true", "1", "si", "sí", "yes"
            )

            casos.append((
                fila["usuario"],
                fila["clave"],
                debe_funcionar,
                fila["descripcion"]
            ))

    return casos


def leer_json_productos(ruta_archivo=None):
    """Lee los productos desde un archivo JSON."""
    if ruta_archivo is None:
        ruta_archivo = CARPETA_DATOS / "productos.json"

    with open(ruta_archivo, mode="r", encoding="utf-8-sig") as archivo:
        return json.load(archivo)
