# Plan de datos y licencias · Equipo 5 Green

## 1. Fuentes y licencias
- **Fuente principal:** `PlantVillage-Dataset` (`https://github.com/spMohanty/PlantVillage-Dataset`), repositorio público de imágenes de hojas de cultivos sanas y enfermas. Debemos revisar directamente en el repositorio de GitHub y en la documentación original de PlantVillage las condiciones/licencia de uso antes de entrenar en producción o redistribuir datos, sin dar por válida una licencia inventada.
- **Respaldo de desarrollo en Colab:** generación sintética reproducible (`SEMILLA = 42`) cuando aún no se haya clonado `data/PlantVillage-Dataset` en la sesión, claramente identificada como respaldo sintético.
- **Datos personales:** no se incluyen datos personales de personas ni datos privados de clientes.

## 2. Variables y estructura
- Imágenes de hojas agrupadas en clases (`sana` frente a `enferma`, conservando el nombre de subcarpeta original de `PlantVillage-Dataset` como subgrupo/cultivo/enfermedad), dimensiones (`ancho`, `alto`), `brillo`, `contraste`, `indice_verdor` y hash `MD5`.

## 3. Calidad del dato (EDA)
- En `01_eda.ipynb` comprobamos imágenes dañadas/nulas, duplicados exactos (`MD5`), equilibrio entre hojas sanas y enfermas, distribución por subcarpetas y casos de bajo contraste/iluminación donde el modelo es menos fiable.

## 4. Linaje
`Repositorio PlantVillage-Dataset (spMohanty) -> clonado/carga en data/PlantVillage-Dataset (o respaldo sintético con SEMILLA=42) -> 01_eda.ipynb (calidad y exploración) -> 02_baseline.ipynb (partición estratificada, baseline y regla de no fiarse)`.

## 5. Partición y privacidad
- Partición estratificada (`test_size=0.25`, `random_state=42`) fijada antes de ver resultados finales, calculando umbrales de referencia solo sobre entrenamiento.
- No se suben claves, tokens ni archivos pesados no permitidos por la licencia.