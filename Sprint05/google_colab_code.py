# ==============================================================================
# SPRINT 05: MATES EN CÓDIGO Y GRADIENTE (TURISDATA CANARIAS)
# Equipo: 5Green
# Ejecución en Google Colab
# ==============================================================================

# 1. IMPORTAR LIBRERÍAS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=== SPRINT 05: ANÁLISIS MATEMÁTICO Y DESCENSO DEL GRADIENTE ===")

# ==============================================================================
# ACTIVIDAD 1: ÁLGEBRA Y ESTADÍSTICA DE RESERVAS (NUMPY Y PANDAS)
# ==============================================================================
# Creamos un conjunto de datos simulado de reservas para TurisData
np.random.seed(42)
n_reservas = 100

precios = np.random.uniform(50, 200, n_reservas)  # Precios entre 50€ y 200€
# La demanda (noches) baja a medida que el precio sube (relación inversa + ruido)
noches = np.maximum(1, np.round(12 - 0.04 * precios + np.random.normal(0, 1.5, n_reservas)))

df_turisdata = pd.DataFrame({
    'precio_noche': precios,
    'noches': noches,
    'ingreso_total': precios * noches
})

print("\n--- 1. Estadísticas Descriptivas ---")
print(f"Precio Medio: {df_turisdata['precio_noche'].mean():.2f} €")
print(f"Estancia Media: {df_turisdata['noches'].mean():.2f} noches")
print(f"Ingreso Total Generado: {df_turisdata['ingreso_total'].sum():.2f} €")

# Correlación de Pearson
correlacion = df_turisdata['precio_noche'].corr(df_turisdata['noches'])
print(f"Correlación entre Precio y Noches Reservadas: {correlacion:.4f}")

# ==============================================================================
# ACTIVIDAD 2: DESCENSO DEL GRADIENTE DESDE CERO
# Objetivo: Encontrar la recta y = w * x + b que predice las noches en función del precio.
# ==============================================================================

# Normalización de variables para mejorar la convergencia del gradiente
X = (precios - precios.mean()) / precios.std()
y = noches

# Parámetros iniciales
w = 0.0  # Pendiente inicial
b = 0.0  # Intersección inicial
learning_rate = 0.05  # Tasa de aprendizaje
epochs = 100  # Número de iteraciones

historial_coste = []

# Algoritmo del Descenso del Gradiente
for epoch in range(epochs):
    y_pred = w * X + b
    
    # Error Cuadrático Medio (MSE)
    coste = np.mean((y - y_pred) ** 2)
    historial_coste.append(coste)
    
    # Cálculo de los gradientes (derivadas parciales)
    dw = (-2 / len(X)) * np.sum(X * (y - y_pred))
    db = (-2 / len(X)) * np.sum(y - y_pred)
    
    # Actualización de pesos
    w = w - learning_rate * dw
    b = b - learning_rate * db

print("\n--- 2. Resultados del Descenso del Gradiente ---")
print(f"Peso óptimo (w): {w:.4f}")
print(f"Sesgo óptimo (b): {b:.4f}")
print(f"Coste final (MSE): {historial_coste[-1]:.4f}")

# ==============================================================================
# ACTIVIDAD 3: VISUALIZACIÓN DE RESULTADOS
# ==============================================================================
plt.figure(figsize=(12, 5))

# Gráfica 1: Convergencia del Coste
plt.subplot(1, 2, 1)
plt.plot(range(epochs), historial_coste, color='green', linewidth=2)
plt.title('Convergencia del Coste (MSE)')
plt.xlabel('Época / Iteración')
plt.ylabel('Error Cuadrático Medio')
plt.grid(True)

# Gráfica 2: Ajuste de la Recta de Regresión
plt.subplot(1, 2, 2)
plt.scatter(X, y, color='blue', alpha=0.5, label='Datos reales')
plt.plot(X, w * X + b, color='red', linewidth=2, label=f'Ajuste: y = {w:.2f}x + {b:.2f}')
plt.title('Relación Precio vs Noches Reservadas')
plt.xlabel('Precio Normalizado')
plt.ylabel('Noches Reservadas')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print("\n[OK] Script completado con éxito. Visualizaciones generadas.")