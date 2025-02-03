package solve

import (
    "fmt"
    "time"
)

func operacionesMatriciales(n int) float64 {
    // Crear matrices de prueba
    matrizA := make([][]float64, n)
    matrizB := make([][]float64, n)
    resultado := make([][]float64, n)
    
    for i := 0; i < n; i++ {
        matrizA[i] = make([]float64, n)
        matrizB[i] = make([]float64, n)
        resultado[i] = make([]float64, n)
        
        for j := 0; j < n; j++ {
            matrizA[i][j] = float64(i + j)
            matrizB[i][j] = float64(j - i)
            resultado[i][j] = 0
        }
    }
    
    // Realizar operaciones matriciales básicas
    inicio := time.Now()
    
    // Multiplicación de matrices
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            for k := 0; k < n; k++ {
                resultado[i][j] += matrizA[i][k] * matrizB[k][j]
            }
        }
    }
    
    fin := time.Since(inicio).Seconds() * 1000 // Convertir a milisegundos
    return fin
}

func main() {
    fmt.Printf("Tiempo de ejecución para n=100: %.4f ms\n", 
        operacionesMatriciales(100))
}
