# Simulación HMM para Control de Infracciones Urbanísticas
Este repositorio contiene el código fuente para simular un Modelo Oculto de Markov (HMM) aplicado a la detección de infracciones y ocupación de espacio público, bajo el marco de la Ley 1801 de 2016.

## Requisitos
- Python 3.9+
- Librerías: `numpy`, `scipy`, `matplotlib`

## Ejecución (Fase 5 - Simulación)
Ejecute el script `hmm_simulation.py` para generar las simulaciones de los 3 escenarios con sus respectivas estadísticas (Media, Varianza e Intervalos de Confianza).

## Reproducibilidad
El código cuenta con semillas fijas (`np.random.seed(42)`) para garantizar la total replicabilidad de los resultados (Criterio Q1).
