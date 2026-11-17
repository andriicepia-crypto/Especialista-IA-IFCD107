# Informe Técnico: Análisis de Ocupación Diaria y Factores Determinantes

**Cliente:** TurisData Canarias  
**Sprint 5:** Matemáticas y estadística en código  
**Proyecto:** Reto PBL «¿La ocupación depende de esto?»

---

## 1\. Introducción y Pregunta de Negocio

El presente informe analiza la serie temporal diaria de ocupación de un alojamiento turístico en Canarias ($N=1096$ días, equivalente a 3 años de registros). El objetivo central es responder a los interrogantes planteados por el cliente:

* *¿Cuánto cambia la ocupación diaria cuando hace más calor y cuando el día es festivo?*  
* *¿Debemos planificar personal y precios teniendo en cuenta la temperatura?*

Para garantizar la reproducibilidad y la robustez técnica, los datos brutos han sido ingeridos en una base de datos local SQLite (`turisdata_reto.db`) optimizada mediante índices temporales, procesados mediante descenso del gradiente implementado desde cero en Python (sin librerías de aprendizaje automático de alto nivel) y validados mediante contrastes estadísticos formales con `statsmodels`.

---

## 2\. Ingesta de Datos y Arquitectura de la Base de Datos

Los datos se cargaron desde un archivo fuente CSV hacia una tabla relacional en SQLite denominada `ocupacion_diaria`. Para optimizar las consultas temporales y analíticas, se estableció un índice sobre la columna de fecha:

```sql
CREATE INDEX IF NOT EXISTS idx_ocupacion_fecha ON ocupacion_diaria(fecha);
```

Posteriormente, los datos se consultaron desde Python extrayendo dinámicamente la componente estacional mensual mediante funciones SQL nativas: $$\text{mes} = \text{CAST}(\text{SUBSTR}(\text{fecha}, 6, 2) \text{ AS INTEGER})$$

---

## 3\. Análisis Exploratorio de Datos (EDA)

El análisis descriptivo de la serie de ocupación porcentual (`ocupacion_pct`) revela los siguientes patrones generales:

* **Dispersión y Tendencia Central:** La serie muestra oscilaciones significativas a lo largo del año, fuertemente condicionadas por los flujos estacionales del turismo insular.  
* **Estacionalidad Mensual:** Al agrupar los datos por mes (`groupby("mes")`), se observa que los meses estivales (julio y agosto) y los periodos invernales de alta afluencia europea registran las medias de ocupación más elevadas, superando ampliamente a los meses de transición.

---

## 4\. Modelado Matemático: Descenso del Gradiente desde Cero

Para aislar el impacto real de las variables explicativas, se implementó un algoritmo de regresión lineal basado en el **descenso del gradiente** utilizando el Error Cuadrático Medio (MSE) como función de coste:

$$\text{Gradiente} = \frac{2}{n} X^T (X w - y)$$

Se ajustaron dos modelos diferenciados:

1. **Modelo Simple ($\text{ocupación} \sim \text{temperatura}$):** Al evaluar la relación cruda, se obtuvo una pendiente aparente de $\approx -1.86$ puntos porcentuales por cada grado Celsius adicional. No obstante, este resultado inicial oculta una variable de confusión fundamental: la estacionalidad del calendario.  
2. **Modelo con Control ($\text{ocupación} \sim \text{temperatura} + \text{festivo} + \text{meses}$):** Incorporando variables binarias (*dummies*) para controlar los 11 meses del año y el efecto festivo, el comportamiento térmico cambia radicalmente. La pendiente ajustada de la temperatura se reduce a $\approx -0.09$ puntos por °C, perdiendo significancia estadística. En contraste, el efecto de los días festivos se mantiene sumamente robusto en $\approx +9.11$ puntos de ocupación.

---

## 5\. Validación con Librería Estadística (`statsmodels`)

Para corroborar la corrección matemática de la implementación manual, se ajustaron los mismos modelos utilizando `statsmodels` (`smf.ols`). La tabla comparativa obtenida demuestra una coincidencia exacta hasta el tercer decimal:

| Coeficiente / Efecto | Implementación (Desde Cero) | Librería (`statsmodels`) |
| :---- | :---: | :---: |
| **Pendiente Simple** ($\text{temperatura}$) | $-1.860$ | $-1.860$ |
| **Efecto Temperatura** (Con Control) | $-0.089$ | $-0.089$ |
| **Efecto Festivo** (Con Control) | $+9.111$ | $+9.111$ |

Esta concordancia valida formalmente la precisión del algoritmo de descenso del gradiente programado.

---

## 6\. Inferencia y Contraste Estadístico

El análisis inferencial sobre el modelo multivariante con control aporta los siguientes indicadores clave:

* **Temperatura con control ($p_{\text{temp}}$):** Arroja un p-valor superior a $0.05$ ($p\approx 0.48$), lo que confirma que, una vez descontado el efecto estacional del mes, **la temperatura no ejerce un impacto estadísticamente significativo** sobre la ocupación.  
* **Efecto Festivo (Intervalo de Confianza):** El IC del 95% para los días festivos se sitúa en el rango $[7.35,10.87]$, estimando un incremento medio de $+9.11$ puntos porcentuales.  
* **Prueba t de Welch:** La diferencia de medias entre días festivos y no festivos arroja un p-valor extremadamente minúsculo ($p<1{0}^{-20}$), corroborando la disparidad de ocupación en fechas señaladas.  
* **Bondad de Ajuste (${R}^{2}$):** El coeficiente de determinación del modelo con control es ${R}^{2}\approx 0.58$, lo que indica que el conjunto de variables explicativas logra capturar aproximadamente el $58\%$ de la variabilidad observada en la ocupación diaria.

---

## 7\. Respuesta Ejecutiva al Cliente

> **Resumen para Dirección:** La temperatura no afecta de manera directa a la ocupación ($p\approx 0.48$); el aparente efecto inicial se debe a la estacionalidad de los meses. En cambio, los días festivos incrementan la ocupación en promedio un $+9.11$ puntos (IC 95%: $[7.35,10.87]$).

> **Recomendación:** Planifique personal y tarifas dinámicas priorizando los fines de semana y festivos sobre las variaciones térmicas.

> **Límites:** Estos resultados provienen de datos sintéticos de un único alojamiento y reflejan correlaciones estadísticas, no relaciones causales directas. El modelo explica el $58\%$ de la variabilidad (${R}^{2}\approx 0.58$).

> **IA responsable:** Las recomendaciones automáticas de precios deben ser supervisadas siempre por un gestor humano para evitar desviaciones comerciales imprevistas.

&nbsp;

&nbsp;

# Version corta INFORME:

## **Mi respuesta al cliente:**

&nbsp;

1. **Respuesta directa:** La temperatura no tiene un impacto real en la ocupación ($p\approx 0.48$). En cambio, los días festivos aumentan la ocupación un promedio de **\+9,11 puntos** (con un intervalo de confianza del 95% entre **7,35 y 10,87**).  
2. **Recomendación accionable:** Planifique el personal y las tarifas de precios priorizando los días festivos y fines de semana en lugar del clima.  
3. **Límites:** Se trata de datos sintéticos de un solo alojamiento. El informe refleja correlaciones estadísticas y no causalidad directa, la variable "mes" condiciona el resultado, y el modelo explica el 58% de la variabilidad (${R}^{2}\approx 0.58$).  
4. **IA responsable:** No utilice este modelo para fijar precios de manera automática sin revisión humana ni interprete los resultados como una causa directa.

&nbsp;