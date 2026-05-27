//Questão 9 — Nota com conceito
#include <stdio.h>

int main() {
    float nota;

    printf("Digite a nota: ");
    scanf("%f", &nota);

    if (nota >= 9.0) {
        printf("CONCEITO A\n");
    } else if (nota >= 7.0) {
        printf("CONCEITO B\n");
    } else if (nota >= 5.0) {
        printf("CONCEITO C\n");
    } else {
        printf("CONCEITO D\n");
    }

    return 0;
}