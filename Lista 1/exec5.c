//Questão 5 — Classificação de temperatura
#include <stdio.h>

int main() {
    float temperatura;

    printf("Digite a temperatura: ");
    scanf("%f", &temperatura);

    if (temperatura <= 15) {
        printf("FRIO\n");
    } else if (temperatura <= 30) {
        printf("AGRADAVEL\n");
    } else {
        printf("QUENTE\n");
    }

    return 0;
}