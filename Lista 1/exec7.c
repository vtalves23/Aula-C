//Questão 7 — Intervalo numérico
#include <stdio.h>

int main() {
    int numero;

    printf("Digite um numero inteiro: ");
    scanf("%d", &numero);

    if (numero >= 10 && numero <= 20) {
        printf("DENTRO DO INTERVALO\n");
    } else {
        printf("FORA DO INTERVALO\n");
    }

    return 0;
}