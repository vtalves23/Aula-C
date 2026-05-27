//Questão 8 — Classificação de salário
#include <stdio.h>

int main() {
    float salario;

    printf("Digite o salario: ");
    scanf("%f", &salario);

    if (salario <= 1500) {
        printf("SALARIO BAIXO\n");
    } else if (salario <= 3000) {
        printf("SALARIO MEDIO\n");
    } else {
        printf("SALARIO ALTO\n");
    }

    return 0;
}
