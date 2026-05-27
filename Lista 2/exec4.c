#include <stdio.h>

int main() {
    int numero;

    printf("Digite um numero: ");
    scanf("%d", &numero);

    if (numero <= 10) {
        printf("CATEGORIA A\n");
    } else if (numero <= 20) {
        printf("CATEGORIA B\n");
    } else if (numero <= 30) {
        printf("CATEGORIA C\n");
    } else {
        printf("FORA DA CLASSIFICACAO\n");
    }

    return 0;
}