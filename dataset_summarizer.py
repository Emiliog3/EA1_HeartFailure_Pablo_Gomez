"""Resumen sencillo y reproducible de un DataFrame de pandas.

Actividad 1 - Proyecto Integrado III - Analítica de Datos.
"""

from pathlib import Path
import pandas as pd


class DatasetSummarizer:
    """Construye y guarda un resumen básico del DataFrame recibido."""

    def __init__(self, dataframe: pd.DataFrame) -> None:
        # 1. Trabajamos con una copia para evitar modificar accidentalmente
        # el DataFrame que llega desde el notebook.
        self.dataframe = dataframe.copy()

    def construir_resumen(self) -> str:
        """Devuelve filas, columnas, tipos de datos y valores nulos."""
        # 2. Empezamos con las medidas generales solicitadas en la actividad.
        filas, columnas = self.dataframe.shape
        lineas = [
            "RESUMEN DEL DATAFRAME TRANSFORMADO",
            "=" * 40,
            f"Filas: {filas}",
            f"Columnas: {columnas}",
            f"Valores nulos totales: {int(self.dataframe.isna().sum().sum())}",
            "",
            "DETALLE DE COLUMNAS",
            "-" * 40,
        ]

        # 3. Recorremos las columnas para dejar visible su nombre, tipo y
        # cantidad de valores nulos. Esto facilita revisar la estructura.
        for numero, columna in enumerate(self.dataframe.columns, start=1):
            tipo = self.dataframe[columna].dtype
            nulos = int(self.dataframe[columna].isna().sum())
            lineas.append(
                f"{numero}. {columna} | tipo: {tipo} | nulos: {nulos}"
            )

        return "\n".join(lineas)

    def guardar_resumen(self, ruta_salida: str = "resumen_heart_failure.txt") -> Path:
        """Escribe el resumen en un archivo .txt y devuelve su ruta."""
        # 4. La codificación UTF-8 conserva correctamente tildes y caracteres
        # del texto descriptivo cuando el archivo se abre en Windows o GitHub.
        ruta = Path(ruta_salida)
        ruta.write_text(self.construir_resumen(), encoding="utf-8")
        return ruta
