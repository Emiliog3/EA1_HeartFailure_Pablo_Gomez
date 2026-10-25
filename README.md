# EA1 - Carga y creación de dataset de salud

**Proyecto Integrado III - Analítica de Datos**  
**Estudiante:** Pablo Emilio Gómez Gómez  
**Docente:** Andrés Felipe Callejas Jaramillo  
**Institución:** Institución Universitaria Digital de Antioquia  
**Código del curso:** PREICA2602B020038  
**Actividad:** S10 - EA1 - Carga y Creación de Dataset  
**Fecha:** 25 de octubre de 2026

## Descripción

Este proyecto desarrolla el flujo solicitado en la Actividad 1: obtener un dataset desde Hugging Face, convertirlo en un DataFrame de pandas, realizar transformaciones visibles desde un Jupyter Notebook y generar un archivo `.txt` que permita reconocer la estructura final de los datos.

Se eligió el dataset público `mstz/heart_failure` por ser pequeño, tabular y relacionado con salud. El objetivo del trabajo es demostrar el manejo técnico de datos y control de versiones; no realizar interpretación clínica.

## Estructura del proyecto

```text
EA1_HeartFailure_Pablo_Gomez/
├── .github/
│   └── workflows/
│       └── validacion_python.yml
├── .gitignore
├── METADATA_DATASET.md
├── README.md
├── dataset_summarizer.py
├── hf_dataset_loader.py
├── PABLO_GOMEZ_EA1_CARGA_DATASET.ipynb
├── requirements.txt
└── resumen_heart_failure.txt
```

## Flujo de la actividad

```text
Hugging Face
     ↓
HFDatasetLoader
     ↓
DataFrame original
     ↓
Transformaciones en Jupyter
     ↓
DataFrame transformado
     ↓
DatasetSummarizer
     ↓
resumen_heart_failure.txt
```

## Transformaciones realizadas

La consigna permite una transformación mínima, pero la rúbrica asigna el puntaje máximo cuando el notebook presenta **al menos cuatro transformaciones distintas**. Por esa razón se dejaron cinco operaciones visibles:

1. Renombrar las 13 columnas originales con nombres breves en español.
2. Convertir cinco variables booleanas a valores enteros `0/1`.
3. Crear la variable `grupo_edad` a partir de rangos de edad.
4. Crear el indicador `seguimiento_mayor_100_dias` mediante una condición reproducible.
5. Seleccionar y ordenar las 15 columnas que conforman el DataFrame final.

El resumen `.txt` se genera **después** de estas transformaciones, por lo que corresponde al DataFrame final y no al conjunto original.

## Preparación del entorno

En la terminal de Visual Studio Code, ubicada en la carpeta del proyecto:

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Luego:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecución

1. Abrir `PABLO_GOMEZ_EA1_CARGA_DATASET.ipynb` en Visual Studio Code.
2. Seleccionar como kernel el Python del entorno `.venv`.
3. Ejecutar las celdas en orden desde el inicio.
4. Verificar que la carga muestre **299 filas y 13 columnas** antes de transformar.
5. Confirmar que el resultado final muestre **299 filas y 15 columnas**.
6. Comprobar que se genere `resumen_heart_failure.txt`.

## Cobertura de la rúbrica

| Criterio | Evidencia incluida |
| --- | --- |
| Repositorio y control de versiones | Proyecto inicializado con Git y commits por etapas. |
| Clase para generar DataFrame | `hf_dataset_loader.py` con `HFDatasetLoader`. |
| Clase para resumir y exportar | `dataset_summarizer.py` con `DatasetSummarizer`. |
| Cuatro o más transformaciones | Notebook con cinco transformaciones visibles. |
| Funcionamiento y evidencias | Salidas guardadas en el notebook, validación final y `.txt` generado. |

## Dataset

Hugging Face: https://huggingface.co/datasets/mstz/heart_failure  
Configuración: `death`  
Split: `train`

La página del dataset reporta 299 registros y 13 variables originales. La metadata básica utilizada en el proyecto también se conserva en `METADATA_DATASET.md`.

## Observación académica

Las categorías creadas en el notebook son transformaciones de datos para fines de aprendizaje. No deben interpretarse como diagnóstico, pronóstico o recomendación médica.
