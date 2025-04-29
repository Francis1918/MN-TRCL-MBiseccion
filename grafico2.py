#grafico 2import numpy as np
import matplotlib.pyplot as plt
import numpy as np
# Definir la función original
def f(x):
    return (1/4) * (x**3 + 3*x**2 - 6*x - 8)

# Definir la derivada de la función
def f_derivada(x):
    return (1/4) * (3*x**2 + 6*x - 6)

# Crear un rango de valores para x
x = np.linspace(-5, 5, 500)

# Calcular los valores de f(x) y f'(x)
y = f(x)
y_derivada = f_derivada(x)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = (1/4)(x^3 + 3x^2 - 6x - 8)', color='blue')
plt.plot(x, y_derivada, label="f'(x) = (1/4)(3x^2 + 6x - 6)", color='red', linestyle='--')

# Agregar etiquetas y título
plt.title('Gráfico de f(x) y su derivada f\'(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Eje x
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Eje y
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# Mostrar el gráfico
plt.show()