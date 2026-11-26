# Proyecto Final · Equipo 5 Green

- **Equipo:** 5 Green (Cristina, Miguel, Fran, Andri, Anzhela)
- **Brief:** Salud de cultivos — *«¿Hoja sana o enferma, y cuándo no fiarnos del modelo?»*
- **Base de datos:** `PlantVillage-Dataset` (`https://github.com/spMohanty/PlantVillage-Dataset`)
- **Carpeta del Sprint 14:** https://github.com/cCoolBoox/IFCD107-alumnado/tree/main/sprints/S14

## Cómo ejecutar el Sprint 14
1. Abrir `sprint-14/01_eda.ipynb` en Google Colab.
2. Si queréis usar los datos reales del repositorio, clonar `https://github.com/spMohanty/PlantVillage-Dataset.git` en `data/PlantVillage-Dataset` (o ejecutar directamente con el respaldo sintético de `SEMILLA = 42` si aún no está clonado).
3. Ejecutar `sprint-14/01_eda.ipynb` de arriba abajo para ver calidad, clases (`sana` / `enferma`) y contraste.
4. Ejecutar `sprint-14/02_baseline.ipynb` de arriba abajo para ver partición estratificada, baseline (`F1_macro` y `accuracy`) y la regla de «cuándo no fiarse».
5. Revisar los documentos y hojas individuales de autoevaluación/coevaluación en `sprint-14/`.

## Uso de IA en este sprint
- **Qué pedimos a la IA:** borradores de estructura documental, celdas de exploración/baseline con `SEMILLA = 42` y ejemplos de reglas de confianza.
- **Qué comprobamos a mano:** revisamos el código, comprobamos que la partición no tenga fuga de datos y verificamos que la licencia y los límites de `PlantVillage-Dataset` estén claros.
- **Qué cambiamos:** adaptamos los textos y ejemplos a un lenguaje sencillo de estudiantes y al problema de hojas sanas/enfermas y cuándo no fiarnos.

## Revisión con la rúbrica (Sprint 14)
- **Corrección técnica (Nivel 3–4):** cuadernos `01_eda.ipynb` y `02_baseline.ipynb` ejecutables de arriba abajo con `SEMILLA = 42`, métrica (`F1_macro`) y partición fijadas antes de evaluar, informe de calidad y regla de cuándo no fiarse.
- **Reproducibilidad (Nivel 3–4):** referencia clara a `PlantVillage-Dataset`, respaldo sintético si no está clonado en la sesión, `requirements.txt` y `README.md`.
- **Análisis y comunicación al cliente (Nivel 3–4):** pregunta clara en una frase, cliente, decisión y explicación sencilla de cuándo pedir revisión humana si el modelo duda.
- **IA responsable (Nivel 3–4):** uso de IA declarado y revisado a mano, clasificación RGPD/AI Act y 6 riesgos específicos vinculados al dataset y al cultivo.
```[cite: 35, 36, 40, 41, 43, 45, 47]