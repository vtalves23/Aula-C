#include <stdio.h>

int main() {
    int temDinheiro, conseguiuEmprestimo;

    printf("Tem dinheiro? (1-SIM / 0-NAO): ");
    scanf("%d", &temDinheiro);

    if (temDinheiro == 1) {
        printf("COMPRA\n");
    } else {
        printf("Conseguiu emprestimo? (1-SIM / 0-NAO): ");
        scanf("%d", &conseguiuEmprestimo);

        if (conseguiuEmprestimo == 1) {
            printf("COMPRA\n");
        } else {
            printf("NAO COMPRA\n");
        }
    }

    return 0;
}