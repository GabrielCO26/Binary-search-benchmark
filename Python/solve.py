def operaciones_matriciales(n):
    # Crear matrices de prueba
    matriz_a = [[i + j for j in range(n)] for i in range(n)]
    matriz_b = [[j - i for j in range(n)] for i in range(n)]
    
    # Realizar operaciones matriciales básicas
    import time
    inicio = time.time()
    
    # Multiplicación de matrices
    resultado = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    
    fin = time.time()
    tiempo_ejecucion = (fin - inicio) * 1000  # Convertir a milisegundos
    
    # Guardar el resultado en un archivo
    with open("resultadoPy.txt", "w") as archivo:
        archivo.write(f"Tiempo de ejecución para n={n}: {tiempo_ejecucion:.4f} ms\n")
    
    return tiempo_ejecucion

# Ejecutar la función y guardar el resultado
n = 100
operaciones_matriciales(n)
