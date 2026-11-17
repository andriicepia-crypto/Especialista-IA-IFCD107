# Informe de modelado · TurisData Canarias · «Precio y cancelación»

**Equipo:** … · **Fecha:** 11/11/2026

## 1\. Resumen para el gerente

- **Tarifa de referencia:** con solo el tipo de habitación y la temporada estimamos el precio de una noche con un error medio de **6,8 €** (sobre un precio medio de 103 €).  
- **Aviso de cancelación:** recomendamos marcar como «en riesgo» toda reserva con una probabilidad de cancelar de **0,25 o más**.  
- **Qué cuesta cada error:** una cancelación que no vemos venir cuesta **284 €** (noches vacías). Una falsa alarma cuesta **103 €** (reubicar al cliente).  
- **Lo que ahorra:** en 1.200 reservas de prueba, los errores cuestan **58.331 €** con el aviso y **156.484 €** sin él: **98.153 € menos (−63 %)**, unos **82 € por reserva**.  
- La recomendación se mantiene aunque nuestros costes se desvíen ×2 o ÷2: el umbral solo pasa a estar entre 0,15 y 0,40.  
- **Límite:** son datos sintéticos de un solo hotel. Antes de sobrevender de verdad, conviene una prueba piloto.

## 2\. Datos y variables

- **Datos:** 6.000 reservas sintéticas (`reservas_turisdata.csv`), 18 columnas más 2 derivadas: `mes_llegada` y `temporada_alta`, que vale 1 en ene, feb, mar, jul, ago y dic. El 45,9 % de las reservas se canceló.  
- **Partición:** 80 % train (4.800) y 20 % test (1.200), con `random_state = 42`. En la clasificación la partición está estratificada por `cancelada`, así que hay un 45,9 % de canceladas en las dos partes.

| Modelo | Variables usadas | Excluidas y por qué |
| :---- | :---- | :---- |
| Precio | `tipo_habitacion` (dummies; la base es la estándar), `temporada_alta` | `cancelada`: **fuga**, porque no se conoce al reservar. `id_reserva`: es un identificador. Las fechas se resumen en `temporada_alta`. El resto se conoce al reservar, pero con todas las columnas el MAE solo baja de 7,24 € a \~7,23 €, así que no compensa. |
| Cancelación | Numéricas: `antelacion_dias`, `noches`, `adultos`, `ninos`, `precio_noche`, `peticiones_especiales`, `cliente_repetidor`, `cancelaciones_previas`, `temporada_alta`. Categóricas: `tipo_habitacion`, `regimen`, `canal`, `pais_origen`, `tarifa`, `deposito` | `cancelada` es la variable objetivo. `id_reserva` y las fechas brutas quedan fuera. Todas las usadas se conocen en el momento de reservar. |

La preparación (imputación, escalado y one-hot) va dentro de un `Pipeline`, de modo que solo se ajusta con train.

## 3\. Regresión: precio por noche

| Modelo | MAE (€) | RMSE (€) | R² |
| :---- | :---- | :---- | :---- |
| Baseline (media) | 25,56 | 33,33 | −0,002 |
| Lineal | 7,24 | 9,70 | 0,915 |
| **Lineal con interacciones** (tipo × temporada) | **6,76** | **8,94** | **0,928** |

**Lectura para el cliente** (modelo lineal):

- Una estándar en temporada baja sale a **67 €**.  
- Suplementos: **superior \+28 €**, **familiar \+45 €**, **suite \+101 €**, y la **temporada alta añade \+22 €**.  
- El modelo con interacciones muestra que la temporada alta no sube igual a todas las habitaciones: \+17,5 € en la estándar, \+23 € en la superior, \+28 € en la familiar y **\+37 € en la suite**. Por eso es el que elegimos. Mejora 0,5 € de MAE y sigue siendo una tarifa fácil de explicar.

**Lo que significa:** «Nos equivocamos de media en 6,8 € por noche». Es aceptable para una tarifa de referencia, porque es un 6–7 % del precio medio.

**Dónde falla (residuos en test):**

- El error crece con el precio: 4–6 € en la estándar, 8 € en la superior y la familiar, y **15 € en la suite en temporada alta**.  
- Solo el 3,3 % de las reservas tiene un error de más de 20 €.  
- Recomendamos revisar a mano las suites de temporada alta.

## 4\. Clasificación: cancelación

Resultados en test (se usó una sola vez):

| Modelo | AUC | AP | Recall (umbral) | Precisión (umbral) |
| :---- | :---- | :---- | :---- | :---- |
| Baseline (siempre «no cancela») | 0,500 | 0,459 | 0 % | — |
| Logística, umbral 0,5 | 0,746 | 0,729 | 62 % | 66 % |
| **Logística, umbral 0,25 (elegido)** | **0,746** | **0,729** | **92 %** | **53 %** |
| k-NN (k \= 25), umbral 0,35 | 0,697 | 0,657 | 89 % | 52 % |

Nos quedamos con la logística. Ordena mejor el riesgo que k-NN (AUC 0,75 frente a 0,70), cuesta menos (58.331 € frente a 64.008 € en test) y es explicable.

**Matriz de confusión en test (umbral 0,25):**

|  | El modelo dice: se mantiene | El modelo dice: cancela |
| :---- | :---- | :---- |
| **Se mantuvo** | VN \= 204 | FP \= 445 |
| **Canceló** | FN \= 44 | VP \= 507 |

El modelo detecta 507 de 551 cancelaciones. A cambio, da 445 falsas alarmas: avisamos mucho porque una noche vacía cuesta casi el triple que una reubicación.

**Factores de riesgo** (odds ratios de la logística; en las numéricas, por cada desviación típica):

- **Aumentan el riesgo:**  
  - Reservar con mucha **antelación**: ×2,1 por cada 62 días más.  
  - Reservar **sin depósito**: ×2,0, unas 4 veces más riesgo que con depósito total.  
  - Reservar por **web intermediaria**: ×1,7.  
  - Reservar una **suite** (×1,5) o en **temporada alta** (×1,3).  
- **Reducen el riesgo:**  
  - La **tarifa no reembolsable** (×0,44).  
  - El **depósito total** (×0,46).  
  - El **canal directo** (×0,55).  
  - Un **precio por noche** más alto (×0,62).

## 5\. De las métricas a los euros

- **Coste de una cancelación no prevista (FN): 284 € por reserva.** Una reserva media dura 5,5 noches a 102,87 €, y suponemos que solo se revende la mitad de esas noches: 0,5 × 5,52 × 102,87 ≈ 284 €.  
- **Coste de una falsa alarma (FP): 103 € por reserva.** Si sobre vendemos y el cliente sí viene, lo reubicamos en otro alojamiento y le damos una compensación, lo que equivale a una noche media.  
- **Umbral elegido con validación cruzada:** 0,25. Lo calculamos con validación cruzada de 5 particiones sobre train, probando de 0,05 a 0,95 en pasos de 0,05 y quedándonos con el de menor coste. La curva de coste tiene forma de U y un mínimo claro.  
- **Coste en test:** sin modelo, **156.484 €** · umbral 0,5, **78.439 €** · umbral elegido, **58.331 €**. Frente a no hacer nada ahorramos **98.153 € (63 %)**, y frente al 0,5 «por defecto», 20.108 €.

**Análisis de sensibilidad** (costes en train con validación cruzada, 4.800 reservas; sirven para comparar hipótesis entre sí, no con el test):

| Hipótesis | FN (€) | FP (€) | Umbral óptimo | Coste con umbral óptimo | Coste si mantenemos 0,25 | Sin modelo | Ahorro |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **La nuestra** | 284 | 103 | **0,25** | 223.121 | 223.121 | 625.652 | 64 % |
| FN el doble | 568 | 103 | 0,15 | 249.011 | 270.833 | 1.251.304 | 80 % |
| FN la mitad | 142 | 103 | 0,40 | 177.360 | 199.265 | 312.826 | 43 % |
| FP la mitad | 284 | 51,5 | 0,15 | 124.506 | 135.416 | 625.652 | 80 % |
| FP el doble | 284 | 206 | 0,40 | 354.720 | 398.530 | 625.652 | 43 % |

**Conclusión:**

- Si la compensación por falsa alarma costara el doble (206 €), el umbral óptimo subiría a 0,40 y el ahorro bajaría al 43 %.  
- La recomendación **se mantiene**: el modelo ahorra dinero en todas las hipótesis.  
- Equivocarnos de umbral por usar 0,25 cuesta como mucho un 12 % más que el óptimo.  
- La cifra que más mueve la decisión es el coste de la falsa alarma. Es la primera que hay que medir con datos reales del hotel.

## 6\. Recomendación de negocio

1. **Clasificar el riesgo en la reserva.** Toda reserva con una probabilidad de 0,25 o más se marca como «en riesgo». Con nuestros datos, eso es el 79 % de las reservas.  
2. **No sobrevender a ciegas: usar la señal en dos niveles.**  
   - *Riesgo medio (0,25–0,5):* recordatorio y confirmación unos días antes de la llegada, y ofrecer cambiar a tarifa no reembolsable o con depósito con un pequeño descuento. Esto ataca justo los factores que más reducen el riesgo.  
   - *Riesgo alto (≥ 0,5):* son el 43 % de las reservas y el 66 % de ellas se cancela. Aquí se puede admitir *overbooking* limitado, por ejemplo una habitación extra por cada 3–4 reservas de riesgo alto el mismo día y en el mismo tipo de habitación, con un acuerdo previo de reubicación con un alojamiento cercano para mantener el coste de la falsa alarma en unos 103 €.  
3. **Beneficio esperado:** con nuestras hipótesis, unos **82 € por reserva**, lo que da **\~82.000 € por cada 1.000 reservas** frente a no actuar.  
4. **Tarifa de referencia:** usar el modelo con interacciones como precio base (estándar 67 €, más los suplementos del apartado 3\) y revisar a mano las suites de temporada alta.

**Límites:**

- Los datos son sintéticos y de un solo hotel.  
- Los costes son hipótesis nuestras, no cifras contables.  
- El modelo ordena mal 1 de cada 4 pares de reservas (AUC 0,75).  
- Si el hotel cambia su política de depósitos, los clientes cambiarán de comportamiento y habrá que reentrenar.  
- No hemos validado en el tiempo: no hemos entrenado con un año y probado con el siguiente.  
- No contamos la pérdida de reputación de una reubicación, más allá de los 103 €.

## 7\. IA responsable

**Riesgos detectados con datos** (proporción de clientes que **no** cancelaron y aun así recibieron aviso, en test):

- **Por canal:** web intermediaria **85 %**, empresa 74 %, agencia 65 %, directo 49 %. Quien reserva por una web intermediaria tiene casi el doble de probabilidad de ser tratado como «sospechoso» sin serlo.  
- **Por depósito:** sin depósito **86 %**, parcial 61 %, total 34 %.  
- **Por país:** es bastante homogéneo, entre el 59 % (NL) y el 71 % (nórdicos). No vemos una penalización clara por nacionalidad, pero algunos grupos son pequeños (29–45 clientes).  
- **Quién sufre los falsos positivos:** el cliente reubicado. Llega y no tiene habitación, aunque cumplió.  
- **Uso indebido:** el modelo podría usarse para exigir depósitos o subir precios solo a ciertos perfiles (país, canal), y eso sería discriminación de precio.

**Medidas que proponemos o hemos aplicado:**

1. El aviso **no cambia el precio ni las condiciones** de un cliente concreto. Solo se usa para la gestión interna de capacidad y para enviar recordatorios a todos por igual.  
2. Si hay que reubicar, primero a quien tenga peor condición contractual (tarifa flexible sin depósito), nunca según el país. La compensación es igual para todos y está pactada de antemano.  
3. Revisar cada trimestre la tasa de falsas alarmas por canal y por país, y alertar si un grupo supera en más de 15 puntos a la media.  
4. Hemos dejado `pais_origen` en el modelo porque apenas pesa (odds 0,8–1,15). Proponemos probar a quitarlo y comprobar que el coste casi no cambia.

**Uso de la IA en el trabajo:** lo detallamos en el README (qué se pidió, qué se revisó y qué se cambió). Las hipótesis de coste y el umbral son nuestros y salen del cálculo, no de la IA.

## 8\. Cómo reproducirlo

- **Versiones:** Python 3.13 · pandas 3.0 · numpy 2.5 · scikit-learn 1.9 · matplotlib 3.11. En Colab, las versiones las imprime la última celda.  
- **Semilla:** `SEMILLA = 42`, que se usa en `train_test_split` y `StratifiedKFold`.  
- **Orden de ejecución:** abrir `reto_S07.ipynb` en Colab y hacer *Entorno de ejecución → Reiniciar y ejecutar todo*. El CSV se descarga solo con `dato()`. El orden de las celdas es: datos y costes → precio → cancelación (validación cruzada para el umbral, y después el test una sola vez) → odds ratios → sensibilidad → IA responsable → versiones.

---

## Revisión con la rúbrica

> Rúbrica completa en `entrega_y_rubrica.md` de la carpeta `2_Entregar` del sprint, apartado 3\. La rellena quien revisa y no escribió esa parte. Hay que ejecutar el cuaderno de arriba abajo solo con el README, leer el informe como si fueras el gerente, mirar el cuaderno (variables, umbral, test) y poner nivel con prueba.

**Revisado por:** … · **Fecha:** \<dd/mm/aaaa\>

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
| :---- | :---- | :---- |
| Corrección técnica |  |  |
| Reproducibilidad |  |  |
| Análisis y comunicación al cliente |  |  |
| IA responsable |  |  |

**Lo primero que mejoraríamos:** …