#include <iostream>
#include <chrono>

double operacionesMatriciales(int n) {
    // Crear matrices de prueba
    double** matriz_a = new double*[n];
    double** matriz_b = new double*[n];
    double** resultado = new double*[n];
    
    for (int i = 0; i < n; i++) {
        matriz_a[i] = new double[n];
        matriz_b[i] = new double[n];
        resultado[i] = new double[n];
        
        for (int j = 0; j < n; j++) {
            matriz_a[i][j] = i + j;
            matriz_b[i][j] = j - i;
            resultado[i][j] = 0;
        }
    }
    
    // Realizar operaciones matriciales básicas
    auto inicio = std::chrono::high_resolution_clock::now();
    
    // Multiplicación de matrices
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j];
            }
        }
    }
    
    auto fin = std::chrono::high_resolution_clock::now();
    double tiempo_ms = std::chrono::duration_cast<std::chrono::microseconds>(fin - inicio).count() / 1000.0;
    
    // Liberar memoria
    for (int i = 0; i < n; i++) {
        delete[] matriz_a[i];
        delete[] matriz_b[i];
        delete[] resultado[i];
    }
    delete[] matriz_a;
    delete[] matriz_b;
    delete[] resultado;
    
    return tiempo_ms;
}

int main() {
    std::cout << operacionesMatriciales(100) << " ms\n";
    return 0;
}
