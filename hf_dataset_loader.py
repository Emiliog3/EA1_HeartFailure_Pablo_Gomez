"""Carga de datasets públicos de Hugging Face a un DataFrame de pandas.

Actividad 1 - Proyecto Integrado III - Analítica de Datos.
"""

from typing import Optional
import pandas as pd


class HFDatasetLoader:
    """Obtiene un dataset de Hugging Face y lo entrega como DataFrame."""

    def __init__(
        self,
        dataset_id: str,
        split: str = "train",
        config_name: Optional[str] = None,
    ) -> None:
        # 1. Guardamos los datos necesarios para localizar el dataset.
        # Así la misma clase puede reutilizarse con otras fuentes de Hugging Face.
        self.dataset_id = dataset_id
        self.split = split
        self.config_name = config_name

    def cargar(self) -> pd.DataFrame:
        """Conecta con Hugging Face, carga el split y lo convierte a pandas."""
        # 2. La importación se hace aquí para que el mensaje de error sea claro
        # cuando la librería `datasets` todavía no está instalada.
        try:
            from datasets import load_dataset
        except ImportError as exc:
            raise ImportError(
                "Falta la librería 'datasets'. Instálala con: pip install -r requirements.txt"
            ) from exc

        # 3. Algunos datasets tienen una configuración interna y otros no.
        # Este bloque permite trabajar correctamente en ambos casos.
        if self.config_name:
            dataset = load_dataset(
                self.dataset_id,
                self.config_name,
                split=self.split,
            )
        else:
            dataset = load_dataset(
                self.dataset_id,
                split=self.split,
            )

        # 4. El objeto de Hugging Face se convierte a DataFrame para que pueda
        # manipularse directamente desde pandas en el notebook.
        dataframe = dataset.to_pandas()
        return dataframe
