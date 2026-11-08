# Simulación HMM para Control de Infracciones Urbanísticas

Este repositorio contiene el código fuente y la documentación para simular un Modelo Oculto de Markov (HMM) aplicado a la detección de infracciones y ocupación de espacio público. El modelo está fundamentado en la **Ley 1801 de 2016** (Código Nacional de Seguridad y Convivencia Ciudadana) y el **Decreto 1077 de 2015** (Licencias Urbanísticas e Intervención del Espacio Público), con el objetivo de optimizar los operativos de inspección municipal mediante enfoques predictivos.

El proyecto fue desarrollado como evidencia de aprendizaje para la materia de Simulación en Ingeniería de Software y Datos.

## 🗂️ Estructura del Proyecto

- `hmm_simulation.py`: Script principal en Python con la lógica estocástica y la simulación Monte Carlo.
- `main.tex`: Documento de investigación en formato LaTeX con el marco teórico, diseño experimental y análisis estadístico.
- `fig1_boxplot.png` y `fig2_evolution.png`: Salidas gráficas generadas por el script.

## 📋 Requisitos Previos

Para ejecutar la simulación, necesitas tener instalado Python (versión 3.9 o superior) y las siguientes librerías:

- `numpy` (Para generación de números pseudoaleatorios y operaciones matriciales)
- `scipy` (Para cálculos estadísticos e intervalos de confianza)
- `matplotlib` (Para la generación y guardado de gráficas)

Puedes instalar todas las dependencias ejecutando el siguiente comando en tu terminal:

```bash
pip install numpy scipy matplotlib
```

## 🚀 Ejecución (Fase 4 y 5 - Implementación y Simulación)

Para correr la simulación, abre tu terminal en la carpeta del repositorio y ejecuta el script principal:

```bash
python hmm_simulation.py
```

### ¿Qué hace el script?
1.  **Simula 3 Escenarios Administrativos:** Escenario Base, Control Estricto y Control Laxo (100 iteraciones de 52 semanas cada uno).
2.  **Imprime Resultados:** Muestra en la consola las métricas estadísticas calculadas para cada escenario (Media, Varianza, etc.).
3.  **Genera Gráficas:** Crea automáticamente dos archivos de imagen en alta resolución (calidad Q1 - 300dpi):
    *   `fig1_boxplot.png`: Diagrama de cajas comparando la permanencia en infracción grave entre los tres escenarios.
    *   `fig2_evolution.png`: Serie de tiempo mostrando la convergencia de las probabilidades de estado en el escenario base.

## 🔬 Reproducibilidad (Criterio Q1)

Con el fin de garantizar el rigor científico y la total replicabilidad de los resultados publicados en el documento de investigación, el código cuenta con una inicialización de aleatoriedad controlada utilizando semillas fijas (`np.random.seed(42)`). Esto asegura que cualquier persona que ejecute el script obtendrá exactamente las mismas estadísticas y gráficas presentadas en el informe final.