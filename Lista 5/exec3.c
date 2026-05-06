#include <stdio.h>

int main() {
    int opcao;
    float saldo = 1000.00, deposito;

    do {
        printf("\nMENU\n");
        printf("1 - Consultar saldo\n");
        printf("2 - Depositar\n");
        printf("0 - Sair\n");
        printf("Qual a opcao: ");
        scanf("%d", &opcao);

        if (opcao == 1) {
            printf("Seu saldo atual e: %.2f\n", saldo);
        } else if (opcao == 2) {
            printf("Digite o valor do deposito: ");
            scanf("%f", &deposito);
            saldo += deposito;  
            printf("Deposito realizado com sucesso!\n");
        } else if (opcao != 0) {
            printf("Opcao invalida!\n");
        }

    } while (opcao != 0);

    printf("Programa encerrado.\n");

    return 0;
}