from scipy.stats import geom
import numpy as np
import statistics
import matplotlib.pyplot as plt

p = 0.08
sample_sizes = [10**2, 10**3, 10**4, 10**5]

data_summary = []

fig, axs = plt.subplots(4, 2, figsize=(14, 20))
fig.suptitle("Ejercicio 2: Distribución Geométrica para Diferentes Tamaños de Muestra")

for i, size in enumerate(sample_sizes):
    sample = geom.rvs(p, size=size)

    median = np.median(sample)
    mode = statistics.mode(sample)
    mean = np.mean(sample)
    variance = np.var(sample)

    data_summary.append({
        "Tamaño de muestra": size,
        "Mediana": median,
        "Moda": mode,
        "Media": mean,
        "Varianza": variance
    })

    axs[i, 0].boxplot(sample)
    axs[i, 0].set_title(f"Diagrama de Cajas - Tamaño de Muestra {size}")
    axs[i, 0].set_ylabel("Valores")

    axs[i, 1].hist(sample, bins=30, color="skyblue", edgecolor="black")
    axs[i, 1].set_title(f"Histograma - Tamaño de Muestra {size}")
    axs[i, 1].set_xlabel("Valores")
    axs[i, 1].set_ylabel("Frecuencia")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

for summary in data_summary:
    print(summary)

# La media teórica de una distribución geométrica es 1/p
# La varianza teórica es (1 - p) / p**2
mean_theoretical = 1 / p
variance_theoretical = (1 - p) / p**2

print(f"\nMedia teórica: {mean_theoretical}")
print(f"Varianza teórica: {variance_theoretical}\n")

for summary in data_summary:
    print(f"Tamaño de muestra: {summary['Tamaño de muestra']}")
    print(f"Media empírica: {summary['Media']} - Diferencia con la teórica: {abs(summary['Media'] - mean_theoretical)}")
    print(f"Varianza empírica: {summary['Varianza']} - Diferencia con la teórica: {abs(summary['Varianza'] - variance_theoretical)}")
    print("----------")
