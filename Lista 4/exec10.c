//Leia 5 números e determine o maior e o menor.
#include <stdio.h>

int main() {
    int numero;
    int maior, menor;

    printf("Digite 5 numeros inteiros:\n");

    // Lendo o primeiro numero separadamente para inicializar as variaveis
    printf("Digite o 1º numero: ");
    scanf("%d", &numero);
    maior = numero;
    menor = numero;

    // O laço roda mais 4 vezes para ler os numeros restantes
    for (int i = 2; i <= 5; i++) {
        printf("Digite o %dº numero: ", i);
        scanf("%d", &numero);

        // Verifica se o numero atual é maior que o maior cadastrado até agora
        if (numero > maior) {
            maior = numero;
        }

        // Verifica se o numero atual é menor que o menor cadastrado até agora
        if (numero < menor) {
            menor = numero;
        }
    }

    // Exibe os resultados
    printf("\n--- Resultado ---\n");
    printf("O maior numero digitado foi: %d\n", maior);
    printf("O menor numero digitado foi: %d\n", menor);

    return 0;
}