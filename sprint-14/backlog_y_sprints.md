# Backlog y planificación de sprints · Equipo 5 Green · Papas Canarias

- **Proyecto:** Monitoreo de la salud de las papas Canarias («¿Hoja sana o enferma, y cuándo no fiarnos del modelo?»)
- **Scrum Master (Sprint 14):** Miguel

## 1. Historias de usuario (12 historias)
| ID | Historia de usuario | Criterio de aceptación | Tamaño | Sprint | Responsable | Estado |
|---|---|---|---|---|---|---|
| H1 | Como responsable de datos quiero reunir y organizar las fotos de papas Canarias (sana/enferma) con su licencia y respaldo reproducible | Carpeta/flujo definido en `plan_datos_licencias.md` y `01_eda.ipynb` | M | 14 | Andri | hecho |
| H2 | Como analista quiero hacer el EDA para revisar nulos, duplicados, reparto de clases y contraste | Cuaderno `01_eda.ipynb` ejecutable con informe y 3 gráficos | M | 14 | Fran | hecho |
| H3 | Como equipo quiero fijar la partición estratificada y `F1_macro` antes de ver resultados finales | Regla de partición y `F1_macro` anotadas antes del baseline | S | 14 | Miguel | hecho |
| H4 | Como responsable técnico quiero construir un baseline simple y un modelo base con regla de no fiarse | Cuaderno `02_baseline.ipynb` ejecutable con métricas y aviso de duda | M | 14 | Fran | hecho |
| H5 | Como responsable de IA responsable quiero registrar los riesgos éticos y normativos de papas Canarias | Documento `riesgos_eticos.md` con RGPD, AI Act y ≥ 5 riesgos específicos | S | 14 | Cristina | hecho |
| H6 | Como equipo quiero tener el repositorio ordenado con README, requirements.txt y commits del equipo | Archivos en su ruta y commits repartidos entre integrantes | S | 14 | Anzhela | en curso |
| H7 | Como responsable técnico quiero entrenar un modelo de aprendizaje automático clásico sobre características de hoja | Modelo entrenado y registrado con `F1_macro` y matriz de confusión | M | 15 | Fran | por hacer |
| H8 | Como responsable técnico quiero entrenar una red neuronal (`CNN` / transferencia) para clasificar hojas de papa | Red neuronal entrenada con semilla fija y comparada en validación | L | 15 | Fran | por hacer |
| H9 | Como equipo quiero comparar al menos 3 modelos en una tabla común y elegir un candidato | Registro de experimentos y modelo candidato justificado | M | 15 | Miguel | por hacer |
| H10 | Como persona que revisa el cultivo quiero ver cuándo el modelo no es fiable (baja confianza o foto oscura/borrosa) | Regla de abstención/revisión probada en casos difíciles y dudosas | M | 16 | Cristina | por hacer |
| H11 | Como cliente quiero probar una demo sencilla con una foto de hoja de papa canaria y ver el resultado y la advertencia | Demostrador funcional (o vídeo de 90 s como respaldo) | L | 16 | Anzhela | por hacer |
| H12 | Como equipo quiero redactar la memoria técnica, preparar la presentación (≤ 12 diapositivas) y ensayar la defensa | Memoria completa, presentación lista y defensa ensayada | M | 17 | Miguel | por hacer |

## 2. Objetivos por sprint
| Sprint | Objetivo medible |
|---|---|
| Sprint 14 | Ficha, plan de datos, `01_eda.ipynb`, `02_baseline.ipynb`, backlog, plan ético y repositorio listos para papas Canarias |
| Sprint 15 | Al menos 3 modelos (incluida red neuronal) entrenados, comparados con registro de experimentos y candidato elegido |
| Sprint 16 | Evaluación completa con gráficos, análisis de cuándo no fiarse, demostrador listo y memoria técnica redactada |
| Sprint 17 | Presentación de ≤ 12 diapositivas terminada, ensayo realizado y defensa oral completada por todo el equipo |

## 3. Retrospectiva (Sprint 14)
| Sprint | Qué seguir haciendo | Qué cambiar | Acción concreta para el siguiente sprint | ¿Se cumplió la acción anterior? |
|---|---|---|---|---|
| Sprint 14 | Trabajar coordinados y comprobar el código paso a paso en Colab | Repartir antes las subidas y revisiones para no dejarlo para el final | Cada persona revisa y sube su parte o comprobación al menos 24 h antes del cierre del sprint | - |