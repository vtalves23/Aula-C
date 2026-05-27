//Leia 10 números e conte positivos, negativos e zeros.
#include <stdio.h>

int main() {
    int numero;
    int positivos = 0;
    int negativos = 0;
    int zeros = 0;

    printf("Digite 10 numeros inteiros:\n");

    // O laço vai rodar exatamente 10 vezes (de 1 a 10)
    for (int i = 1; i <= 10; i++) {
        printf("Digite o %dº numero: ", i);
        scanf("%d", &numero);

        // Verifica a categoria do número
        if (numero > 0) {
            positivos++; // Incrementa 1 aos positivos
        } 
        else if (numero < 0) {
            negativos++; // Incrementa 1 aos negativos
        } 
        else {
            zeros++;     // Se não for maior nem menor que zero, só pode ser zero
        }
    }

    // Exibe os resultados finais
    printf("\n--- Resultado Contagem ---\n");
    printf("Positivos: %d\n", positivos);
    printf("Negativos: %d\n", negativos);
    printf("Zeros: %d\n", zeros);

    return 0;
}