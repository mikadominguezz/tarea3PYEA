# Importamos las librerías necesarias
from scipy.stats import binom
import numpy as np
import statistics
import matplotlib.pyplot as plt

# Parámetros de la distribución binomial
n = 100
p = 0.35
sample_sizes = [10**2, 10**3, 10**4, 10**5]

# Almacenamos los resultados en un diccionario
data_summary = []

# Configuración para visualizar los gráficos
fig, axs = plt.subplots(4, 2, figsize=(14, 20))
fig.suptitle("Ejercicio 1: Distribución Binomial para Diferentes Tamaños de Muestra")

# Iteramos sobre cada tamaño de muestra
for i, size in enumerate(sample_sizes):
    # Generamos la muestra
    sample = binom.rvs(n, p, size=size)

    # Cálculo de estadísticas
    median = np.median(sample)
    mode = statistics.mode(sample)
    mean = np.mean(sample)
    variance = np.var(sample)

    # Guardamos los resultados
    data_summary.append({
        "Tamaño de muestra": size,
        "Mediana": median,
        "Moda": mode,
        "Media": mean,
        "Varianza": variance
    })

    # Diagrama de cajas
    axs[i, 0].boxplot(sample)
    axs[i, 0].set_title(f"Diagrama de Cajas - Tamaño de Muestra {size}")
    axs[i, 0].set_ylabel("Valores")

    # Histograma
    axs[i, 1].hist(sample, bins=30, color="skyblue", edgecolor="black")
    axs[i, 1].set_title(f"Histograma - Tamaño de Muestra {size}")
    axs[i, 1].set_xlabel("Valores")
    axs[i, 1].set_ylabel("Frecuencia")

# Ajustamos el diseño de la figura
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Mostramos los resultados de cada muestra
for summary in data_summary:
    print(summary)

# Cálculo adicional para comparar con la teoría:
# La media teórica de una distribución binomial es n * p
# La varianza teórica es n * p * (1 - p)
mean_theoretical = n * p
variance_theoretical = n * p * (1 - p)

print(f"\nMedia teórica: {mean_theoretical}")
print(f"Varianza teórica: {variance_theoretical}\n")

# Comparación de la media y varianza empírica con la teórica
for summary in data_summary:
    print(f"Tamaño de muestra: {summary['Tamaño de muestra']}")
    print(f"Media empírica: {summary['Media']} - Diferencia con la teórica: {abs(summary['Media'] - mean_theoretical)}")
    print(f"Varianza empírica: {summary['Varianza']} - Diferencia con la teórica: {abs(summary['Varianza'] - variance_theoretical)}")
    print("----------")
