public class solve {
    public static double operacionesMatriciales(int n) {
        // Crear matrices de prueba
        double[][] matriz_a = new double[n][n];
        double[][] matriz_b = new double[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matriz_a[i][j] = i + j;
                matriz_b[i][j] = j - i;
            }
        }
        
        // Realizar operaciones matriciales básicas
        long inicio = System.nanoTime();
        
        // Multiplicación de matrices
        double[][] resultado = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    resultado[i][j] += matriz_a[i][k] * matriz_b[k][j];
                }
            }
        }
        
        long fin = System.nanoTime();
        return (fin - inicio) / 1000000.0;
    }

    public static void main(String[] args) {
        System.out.printf("Java: %.2f ms%n", operacionesMatriciales(100));
    }
}
