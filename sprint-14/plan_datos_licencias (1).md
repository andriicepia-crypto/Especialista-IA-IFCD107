# Plan de datos y licencias

**Proyecto:** ¿Hoja sana o enferma, y cuándo no fiarnos del modelo? Papas Canarias (Equipo 5 Green) · **Responsable de datos:** Andri · **Última actualización:** 26/11/2026

> Sin licencia clara no hay proyecto (R2). Si un dato no tiene licencia, no lo uséis: preguntad al docente.

## 1. Inventario de fuentes

| ID | Nombre del conjunto | Fuente / enlace | Fecha de descarga | Licencia | ¿Permite uso académico / redistribución? | Formato y tamaño | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| D1 | PlantVillage-Dataset | https://github.com/spMohanty/PlantVillage-Dataset | Pendiente / según clonación en sesión | Verificar en el repositorio antes de usar (no asumir licencia) | Revisar condiciones en la fuente original y el repo antes de redistribuir | Imágenes de hojas (JPG/PNG, ~256×256 px en clases de patata) | no |
| D2 | Respaldo sintético reproducible (`SEMILLA = 42`) | Generado en `01_eda.ipynb` / `02_baseline.ipynb` cuando no está clonado `PlantVillage-Dataset` | 26/11/2026 | Uso interno del proyecto / docente | Solo pruebas, desarrollo en Colab y reproducibilidad del sprint | Tabla / métricas sintéticas (1.200 muestras de referencia) | no |

**Licencias frecuentes (orientativo, léelas siempre en la fuente):**
- **CC BY 4.0:** libre uso con atribución. **CC BY-SA:** además, misma licencia al redistribuir. **CC BY-NC:** solo uso no comercial. **CC0:** dominio público.
- **Licencias de datos abiertos de administraciones:** normalmente exigen citar la fuente y la fecha.
- **Kaggle / Hugging Face:** cada conjunto tiene su propia licencia; **no asumas** que es libre.

## 2. Descripción de las variables (diccionario de datos)

| Variable | Tipo | Unidad | Significado | Valores válidos | % nulos |
|---|---|---|---|---|---|
| `archivo` | texto (`str`) | — | Nombre del fichero de imagen de la hoja | Nombres `.jpg` / `.png` válidos | 0 % |
| `subcarpeta` | categórica (`str`) | — | Clase o subcarpeta original en `PlantVillage-Dataset` | Ej. `Potato___healthy`, `Potato___Early_blight`, `Potato___Late_blight` | 0 % |
| `ancho` | entero (`int`) | píxeles (`px`) | Ancho de la imagen en píxeles | `> 0` (habitualmente `256`) | 0 % |
| `alto` | entero (`int`) | píxeles (`px`) | Alto de la imagen en píxeles | `> 0` (habitualmente `256`) | 0 % |
| `brillo` | numérico (`float`) | escala normalizada (`0–1`) | Intensidad lumínica media de la imagen RGB | `[0.0, 1.0]` (`< 0.20` o `> 0.85` alerta de iluminación extrema) | 0 % |
| `contraste` | numérico (`float`) | escala normalizada (`0–1`) | Desviación estándar de intensidad de la imagen | `[0.0, 1.0]` (`< 0.10` alerta de bajo contraste / niebla / borrosidad) | 0 % |
| `verdor` | numérico (`float`) | índice relativo | Índice cromático verde-rojo `(G - R) / (G + R + eps)` | `[-1.0, 1.0]` (valores bajos suelen asociarse a clorosis/manchas) | 0 % |
| `md5` | texto (`str`) | hash hex | Huella MD5 del contenido del archivo para detectar duplicados exactos | Cadena hexadecimal de 32 caracteres | 0 % |
| `hoja_enferma` | binaria (`int`) | `0` / `1` | Etiqueta objetivo agrupada (`0` = hoja sana, `1` = hoja enferma) | `0` (sana) o `1` (enferma) | 0 % |

## 3. Informe de calidad del dato (resumen del EDA)

| Aspecto | Hallazgo | Acción tomada y justificación |
|---|---|---|
| Nulos | `0` nulos en las tablas y características extraídas (imágenes corruptas o ilegibles se filtran durante la lectura) | Comprobar siempre al cargar y descartar cualquier imagen no legible antes de entrenar |
| Duplicados | Posibles duplicados exactos detectados mediante `df.duplicated().sum()` y hash `md5` | Identificar y eliminar duplicados exactos para evitar inflar métricas o colar réplicas entre particiones |
| Valores imposibles / outliers | Imágenes con bajo contraste (`< 0.10`) o brillo extremo (`< 0.20` o `> 0.85`) por sombra, niebla o sub/sobreexposición | No borrar a ciegas si son casos reales difíciles: marcarlos en la regla de **«no fiarse»** para revisión humana |
| Formatos y tipos | Imágenes en distintos formatos/tamaños y columnas numéricas/categóricas en el inventario del EDA | Normalizar a RGB, comprobar dimensiones y fijar tipos explícitos (`int`, `float`, `str`) |
| **Sesgo de muestreo** (¿quién o qué falta en los datos?) | `PlantVillage-Dataset` procede de hojas en condiciones controladas/fondo uniforme y no recoge todas las variedades ni microclimas de papas canarias | Documentar el límite de transferencia a campo en Canarias y contrastar con muestras reales o casos dudosos |
| Desequilibrio de clases / periodos | Diferencia entre el número de imágenes sanas (`0`) y enfermas (`1`) según qué subcarpetas de cultivo/enfermedad se incluyan | Usar partición estratificada (`stratify=y`) y evaluar con `F1_macro` y `Recall` de `hoja_enferma` |
| **Fuga de datos potencial** (variables que no se conocen al decidir) | Usar el nombre de la subcarpeta o archivo donde viene escrita la etiqueta como característica de entrada | Excluir estrictamente nombres de carpeta/archivo etiquetados de `X` y calcular umbrales solo en `train` |

## 4. Linaje del dato (de dónde viene y qué le hemos hecho)

```text
PlantVillage-Dataset (spMohanty) / respaldo sintético SEMILLA=42 → descarga o carga en sesión → inventario y limpieza (MD5, nulos, brillo/contraste/verdor en 01_eda.ipynb) → partición estratificada train/val/test → baseline y regla de no fiarse (02_baseline.ipynb) → modelos y memoria (S15–S17)
```

- Script de descarga / preparación: `sprint-14/descargar_datos.py` y celdas de preparación en `01_eda.ipynb` / `02_baseline.ipynb`.
- **Huella (hash) del conjunto final:** pendiente de registrar al cerrar el conjunto final en `S15_01` (documentando la versión/commit exacto de `PlantVillage-Dataset` o `SEMILLA=42`).
- ¿Se puede recrear todo desde el README? **sí** (siguiendo los pasos de descarga/clonación o ejecutando el respaldo con `SEMILLA = 42` y `requirements.txt`).

## 5. Partición de datos

- Estrategia: **aleatoria estratificada** (`stratify=y`, `SEMILLA = 42`) en `02_baseline.ipynb` (y reservando `test` sin tocar hasta tener candidato).
- Tamaños: entrenamiento **70 %** · validación **15 %** · test **15 %** (**el test no se toca hasta que haya un modelo candidato**, y entonces se mira una sola vez).
- Justificación de por qué evita fugas: estratificar mantiene la proporción de clases (`sana` / `enferma`) en los tres tramos, ajustar modelos y umbrales solo sobre `train`/`val` evita contaminar la evaluación, y dejar `test` intacto hasta el final ofrece una medida limpia de generalización.

## 6. Privacidad y RGPD

- ¿Hay datos personales? **no**.
- ¿Hay datos de menores, salud, biometría u otras categorías especiales? **no** (se trata de sanidad vegetal en hojas de cultivo; si en fases futuras se incorporaran datos de explotaciones o personas identificables, se revisaría con el docente).
- Datos que **no** subiremos al repositorio: carpetas grandes de imágenes descargadas o generadas localmente (`data/`, `datos/`, `*.jpg`, `*.png`, archivos temporales o `.ipynb_checkpoints`), añadidas al `.gitignore`.

## 7. Atribución y cita (pegar tal cual en la memoria)

> Mohanty, S. P., Hughes, D. P., & Salathé, M. *PlantVillage-Dataset* [Repositorio de datos / imágenes]. GitHub: https://github.com/spMohanty/PlantVillage-Dataset (consultado en 2026; verificar licencia y condiciones vigentes en el repositorio antes de su uso o redistribución).
