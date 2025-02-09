const fs = require('fs');  // Importa el módulo 'fs' para trabajar con archivos

function operacionesMatriciales(n) {
    // Crear matrices de prueba
    let matriz_a = Array(n).fill().map((_, i) => 
        Array(n).fill().map((_, j) => i + j)
    );
    
    let matriz_b = Array(n).fill().map((_, i) => 
        Array(n).fill().map((_, j) => j - i)
    );
    
    // Realizar operaciones matriciales básicas
    const inicio = performance.now();
    
    // Multiplicación de matrices
    let resultado = Array(n).fill().map(() => 
        Array(n).fill().map(() => 0)
    );
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            for (let k = 0; k < n; k++) {
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j];
            }
        }
    }
    
    const fin = performance.now();
    return fin - inicio;
}

// Guardar el resultado en un archivo
const tiempo = operacionesMatriciales(100).toFixed(4);
fs.writeFileSync('resultadoJs.txt', `Javascript: ${tiempo} ms\n`);
