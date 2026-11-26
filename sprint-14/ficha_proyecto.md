# Ficha del proyecto · Equipo 5 Green

## 1. Equipo y roles iniciales
- **Equipo:** 5 Green (Cristina, Miguel, Fran, Andri, Anzhela).
- **Roles iniciales:** Scrum Master (Miguel), Responsable técnico (Fran), Responsable de datos (Andri), Responsable de IA responsable (Cristina) y Documentación/entrega (Anzhela), con rotación en cada sprint.

## 2. Brief y pregunta de negocio
- **Brief elegido:** Salud de cultivos («¿Hoja sana o enferma, y cuándo no fiarnos del modelo?»).
- **Pregunta de negocio (en una frase):** Ayudamos al equipo técnico agrícola a decidir qué hojas o lotes revisar o tratar con un modelo que distingue hojas sanas y enfermas e indica cuándo no fiarse de la predicción, medido con `F1_macro` y revisión de casos dudosos frente a un baseline simple.

## 3. Cliente y decisión
- **Cliente:** técnico o responsable de sanidad vegetal / cultivo.
- **Decisión que apoya:** priorizar revisión o tratamiento de hojas enfermas y enviar a inspección humana las imágenes dudosas o de baja calidad.
- **Qué pasa hoy sin el modelo:** revisar fotos o muestras a mano lleva tiempo y varía según la persona o el cansancio.

## 4. Datos
- **Fuente y licencia:** `PlantVillage-Dataset` (`https://github.com/spMohanty/PlantVillage-Dataset`), verificando licencia y condiciones directamente en el repositorio antes de cualquier uso final; respaldo sintético reproducible (`SEMILLA = 42`) si no está clonado en Colab.
- **Tamaño y periodo:** conjunto de imágenes de hojas etiquetadas por condición/enfermedad, agrupables en `sana` y `enferma`.
- **Límites:** fotos tomadas en condiciones de laboratorio o fondo distinto pueden comportarse distinto a fotos reales de campo, con sombras, movimiento o borrosidad.

## 5. Métrica y baseline
- **Métrica de negocio:** menos revisiones perdidas en hojas enfermas y menos decisiones a ciegas en fotos poco claras.
- **Métrica técnica:** `F1_macro` (fijada antes de ver resultados), junto a `accuracy` y matriz de confusión.
- **Umbral de éxito:** superar con claridad al baseline simple (`DummyClassifier` y modelo base) manteniendo marcada la zona de baja confianza/contraste.
- **Baseline previsto:** `DummyClassifier` (`most_frequent`) y modelo base (`02_baseline.ipynb`) con `SEMILLA = 42`.

## 6. Modelos previstos
- Baseline simple (`DummyClassifier`), modelo base de características de color/contraste y red neuronal (`CNN` / transferencia en S15) con regla de cuándo no fiarse.

## 7. Demostrador previsto
- **Tecnología:** cuaderno / demo sencilla en Colab o interfaz web ligera que muestre `sana` o `enferma`, confianza y aviso de «no fiarse / revisar» cuando corresponda (con vídeo de respaldo como plan B).

## 8. Riesgos y mitigación
- **Fotos borrosas, oscuras o de bajo contraste:** marcar `no_fiarse` para revisión humana.
- **Diferencia entre fotos de dataset y fotos reales de campo:** documentar el límite y probar casos difíciles/dudosos.
- **Desequilibrio entre clases o subgrupos:** revisar en EDA y usar partición estratificada y `F1_macro`.
- **Clasificación preliminar AI Act / RGPD:** sin datos personales de personas; sistema de apoyo con supervisión humana en casos dudosos y transparencia sobre sus límites.

## 9. Backlog y objetivos por sprint
- **Sprint 14:** ficha, plan de datos (`PlantVillage-Dataset`), `01_eda.ipynb`, `02_baseline.ipynb`, backlog, plan ético y repositorio.
- **Sprint 15:** al menos 3 modelos comparados (incluida red neuronal) y registro de experimentos.
- **Sprint 16:** evaluación con gráficos, análisis de cuándo no fiarnos, demostrador y memoria técnica.
- **Sprint 17:** presentación (≤ 12 diapositivas), ensayo y defensa oral de todo el equipo.