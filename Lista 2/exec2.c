#include <stdio.h>

int main() {
    float compra;

    printf("Digite o valor da compra: ");
    scanf("%f", &compra);

    if (compra >= 100) {
        printf("RECEBE DESCONTO\n");
    } else {
        printf("NAO RECEBE DESCONTO\n");
    }

    return 0;
}