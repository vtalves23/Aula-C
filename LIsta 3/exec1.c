#include <stdio.h>

int main() {
    int biometria, senha, modoSeguro;

    printf("Digite a biometria (1/0): ");
    scanf("%d", &biometria);

    printf("Digite a senha (1/0): ");
    scanf("%d", &senha);

    printf("Digite o modo seguro (1/0): ");
    scanf("%d", &modoSeguro);

    // Implementação da lógica de desbloqueio
    if (modoSeguro == 1) {
        // Cenário 1: Modo Seguro Ativo -> Exige estritamente a senha
        if (senha == 1) {
            printf("DESBLOQUEADO\n");
        } else {
            printf("BLOQUEADO\n");
        }
    } else {
        // Cenário 2: Modo Seguro Inativo -> Aceita senha OU biometria
        if (biometria == 1 || senha == 1) {
            printf("DESBLOQUEADO\n");
        } else {
            printf("BLOQUEADO\n");
        }
    }

    return 0;
}