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
    return fin - inicio


print(f"Tiempo de ejecución para n=100: {operaciones_matriciales(100):.4f} segundos")
