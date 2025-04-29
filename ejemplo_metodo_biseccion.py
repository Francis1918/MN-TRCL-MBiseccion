#apartir del algoritmo de la bisección
'''
ENTRADA puntos finales a, b; tolerancia TOL; número máximo de iteraciones N₀.
SALIDA solución aproximada p o mensaje de falla.
Paso 1 Sea i = 1;
       FA = f(a).
Paso 2 Mientras i ≤ N₀ haga los pasos 3-6.
Paso 3 Sea p = a + (b - a)/2;  (Calcule pᵢ.)
       FP = f(p).
Paso 4 Si FP = 0 o (b - a)/2 < TOL entonces
       SALIDA (p);  (Procedimiento completado exitosamente.)
       PARE.
Paso 5 Sea i = i + 1.
Paso 6 Si FA · FP > 0 entonces determine a = p;  (Calcule aᵢ, bᵢ.)
       FA = FP
       también determine b = p.  (FA no cambia.)
Paso 7 SALIDA ('El método fracasó después de N₀ iteraciones, N₀ =', N₀);
       (El procedimiento no fue exitoso.)
       PARE.
'''
def metodo_biseccion(f, a, b, TOL, N0):
    i = 1
    FA = f(a)

    while i <= N0:
        p = a + (b - a) / 2  # Calcular pᵢ
        FP = f(p)

        print(f"Iteración {i}: a = {a}, b = {b}, p = {p}, f(p) = {FP}")

        if FP == 0 or (b - a) / 2 < TOL:  # Verificar condición de parada
            print(f"Solución encontrada: p = {p}")
            return p  # Solución encontrada

        i += 1  # Incrementar el contador de iteraciones

        if FA * FP > 0:  # Actualizar los extremos del intervalo
            a = p
            FA = FP
        else:
            b = p

    # Si se alcanza el número máximo de iteraciones sin encontrar solución
    print(f"El método fracasó después de {N0} iteraciones.")
    return f"El método fracasó después de {N0} iteraciones."

# Definir la función para la cual se busca la raíz
def f(x):
    return x**3 - x - 2

# Parámetros del método
a = 1  # Extremo izquierdo del intervalo
b = 2  # Extremo derecho del intervalo
TOL = 1e-5  # Tolerancia
N0 = 100  # Número máximo de iteraciones

# Llamar al método de bisección
resultado = metodo_biseccion(f, a, b, TOL, N0)

# Imprimir el resultado final
print(f"Resultado final: {resultado}")