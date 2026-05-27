#include <stdio.h>

int main() {
    float temperatura;

    printf("Digite a temperatura: ");
    scanf("%f", &temperatura);

    if (temperatura > 30) {
        printf("VAI DE CAMISETA\n");
    } else {
        printf("NAO VAI DE CAMISETA\n");
    }

    return 0;
}