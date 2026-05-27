#include <stdio.h>

int main() {
    float nota, frequencia;

    printf("Digite a nota: ");
    scanf("%f", &nota);

    printf("Digite a frequencia: ");
    scanf("%f", &frequencia);

    if (nota >= 7 && frequencia >= 75) {
        printf("APROVADO\n");
    } else {
        printf("REPROVADO\n");
    }

    return 0;
}