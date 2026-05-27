//Leia números até a soma ultrapassar 100.
#include <stdio.h>

int main() {
    int numero;
    int soma = 0;

    printf("Digite numeros inteiros. O programa para assim que a soma passar de 100.\n");

    // O laço continua enquanto a soma for menor ou igual a 100
    while (soma <= 100) {
        printf("Digite um numero: ");
        scanf("%d", &numero);
        
        soma += numero; // Adiciona o número digitado à soma total
        printf("Soma atual: %d\n", soma);
    }

    printf("\nA soma ultrapassou 100! Soma final: %d\n", soma);

    return 0;
}