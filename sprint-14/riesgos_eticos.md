# Registro de riesgos éticos y normativos · Equipo 5 Green

## 1. Checklist (columna S14)
- Fuente indicada (`PlantVillage-Dataset`) y revisión manual de licencia antes de usar en producción: **Sí**.
- Sin datos personales ni claves en el código o repositorio: **Sí**.
- Regla de «cuándo no fiarnos del modelo» incluida desde el baseline: **Sí**.

## 2. Clasificación RGPD / AI Act
- **RGPD:** no se procesan datos personales de personas en las imágenes de hojas.
- **AI Act:** herramienta de apoyo con supervisión humana cuando el modelo duda o la imagen tiene poca calidad, declarando abiertamente sus límites.

## 3. Riesgos específicos del proyecto (≥ 5)
| ID | Riesgo específico con PlantVillage y cultivos | Probabilidad | Impacto | Medida aplicada | Responsable |
|---|---|---|---|---|---|
| R1 | Fotos con bajo contraste, poca luz o desenfoque provocan errores de clasificación | Alta | Alto | Comprobar contraste/confianza y marcar `no_fiarse` para revisión humana | Fran |
| R2 | El modelo predice con seguridad aparente en hojas de cultivos o fondos distintos a PlantVillage | Alta | Alto | Exigir umbral de confianza (`>= 0.70`) y advertir del límite de dominio | Cristina |
| R3 | Desequilibrio entre cantidad de imágenes sanas y enfermas o entre especies/enfermedades | Media | Medio | Revisar conteos en el EDA, estratificar partición y medir `F1_macro` | Andri |
| R4 | Asumir una licencia sin leer el repositorio original o depender solo de datos de prueba | Media | Alto | Revisar directamente la licencia de `PlantVillage-Dataset` y marcar el respaldo sintético | Andri |
| R5 | Aplicar un tratamiento fitosanitario automático sin revisar casos dudosos | Media | Alto | Mantener revisión humana cuando `no_fiarse` sea verdadero | Miguel |
| R6 | Subir archivos pesados o claves/secretos por error a GitHub | Baja | Alto | Revisar archivos antes de hacer commit y mantener fuera claves o datos no permitidos | Anzhela |