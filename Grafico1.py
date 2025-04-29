import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return (1/6) * x**2 - 4

# Crear un rango de valores para x
x = np.linspace(-10, 10, 500)

# Calcular los valores de f(x)
y = f(x)

# Crear el gráfico
plt.plot(x, y, label='f(x) = (1/6)x^2 - 4', color='blue')

# Agregar etiquetas y título
plt.title('Gráfico de la función f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Eje x
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Eje y
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# Mostrar el gráfico
plt.show()