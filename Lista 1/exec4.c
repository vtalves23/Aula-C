//Questão 4 — Aprovado ou reprovado
#include <stdio.h>

int main() {
    float nota;

    printf("Digite a nota do aluno: ");
    scanf("%f", &nota);

    if (nota >= 7.0) {
        printf("APROVADO\n");
    } else {
        printf("REPROVADO\n");
    }

    return 0;
}