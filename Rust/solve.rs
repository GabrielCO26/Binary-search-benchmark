fn operaciones_matriciales(n: usize) -> f64 {
    // Crear matrices de prueba
    let mut matriz_a: Vec<Vec<f64>> = vec![vec![0.0; n]; n];
    let mut matriz_b: Vec<Vec<f64>> = vec![vec![0.0; n]; n];
    let mut resultado: Vec<Vec<f64>> = vec![vec![0.0; n]; n];
    
    // Primero inicializar matriz_a
    for i in 0..n {
        for j in 0..n {
            matriz_a[i][j] = (i + j) as f64;
        }
    }
    
    // Luego inicializar matriz_b usando valores f64 desde el principio
    for i in 0..n {
        for j in 0..n {
            matriz_b[i][j] = (j as f64) - (i as f64);
        }
    }
    
    // Realizar operaciones matriciales básicas
    let inicio = std::time::Instant::now();
    
    // Multiplicación de matrices
    for i in 0..n {
        for j in 0..n {
            for k in 0..n {
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j];
            }
        }
    }
    
    let duracion = inicio.elapsed().as_secs_f64();
    duracion
}

fn main() {
    println!("Tiempo de ejecución para n=100: {:.4}", 
        operaciones_matriciales(100));
}
