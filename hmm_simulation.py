import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

# Semilla de reproducibilidad (P3)
np.random.seed(42)

# Parámetros Globales
n_sims = 100
n_steps = 52 # Semanas (1 año)

# Matrices de Transición (A)
# S1: Legal, S2: Irregularidad Menor, S3: Infracción Grave/Ocupación
A_base = np.array([[0.85, 0.12, 0.03], 
                   [0.10, 0.70, 0.20], 
                   [0.02, 0.08, 0.90]])

A_strict = np.array([[0.90, 0.08, 0.02], 
                     [0.25, 0.65, 0.10], 
                     [0.15, 0.25, 0.60]])

A_lax = np.array([[0.70, 0.20, 0.10], 
                  [0.05, 0.60, 0.35], 
                  [0.01, 0.04, 0.95]])

# Matriz de Emisión (B)
B = np.array([[0.85, 0.10, 0.05], 
              [0.30, 0.50, 0.20], 
              [0.05, 0.15, 0.80]])

pi = np.array([0.8, 0.15, 0.05])

def simulate_hmm(A):
    s3_proportions = []
    state_history = np.zeros((n_steps, 3))
    
    for _ in range(n_sims):
        state = np.random.choice(3, p=pi)
        s3_count = 0
        for t in range(n_steps):
            state_history[t, state] += 1
            if state == 2: s3_count += 1
            state = np.random.choice(3, p=A[state])
        s3_proportions.append(s3_count / n_steps)
    return s3_proportions, state_history / n_sims

# Ejecutar las simulaciones
print("Ejecutando simulaciones...")
res_base, hist_base = simulate_hmm(A_base)
res_strict, hist_strict = simulate_hmm(A_strict)
res_lax, hist_lax = simulate_hmm(A_lax)

# Mostrar estadísticas en consola
print("\n--- Resultados de Permanencia en Infracción Grave (S3) ---")
print(f"Media Base: {np.mean(res_base):.4f}")
print(f"Media Estricto: {np.mean(res_strict):.4f}")
print(f"Media Laxo: {np.mean(res_lax):.4f}")

# === GENERACIÓN DE GRÁFICAS (Agregado) ===
print("\nGenerando gráficas PNG...")

# 1. Gráfica Boxplot
plt.figure(figsize=(9,6))
plt.boxplot([res_base, res_strict, res_lax], 
            label=['Escenario 1\n(Base)', 'Escenario 2\n(Control Estricto)', 'Escenario 3\n(Control Laxo)'])
plt.ylabel('Proporción de tiempo en Infracción Grave (S3)')
plt.title('Distribución de permanencia en estado de infracción grave por escenario')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('fig1_boxplot.png', dpi=300)
plt.close()
print(" -> 'fig1_boxplot.png' guardada con éxito.")

# 2. Gráfica de Evolución
plt.figure(figsize=(9,6))
plt.plot(hist_base[:,0], label='S1: Cumplimiento Normativo (Con Licencia)', color='#2ca02c', linewidth=2)
plt.plot(hist_base[:,1], label='S2: Irregularidad Menor', color='#ff7f0e', linewidth=2)
plt.plot(hist_base[:,2], label='S3: Ocupación/Infracción Grave', color='#d62728', linewidth=2)
plt.xlabel('Semanas de Simulación (t)')
plt.ylabel('Probabilidad del Estado')
plt.title('Evolución Temporal de Probabilidades de Estado (Escenario Base)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('fig2_evolution.png', dpi=300)
plt.close()
print(" -> 'fig2_evolution.png' guardada con éxito.\nProceso finalizado.")