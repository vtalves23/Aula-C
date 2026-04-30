#include <stdio.h>

int main() {
    int loginOk, dispositivoConhecido, tentativaSuspeita;

    printf("Login correto? (1/0): ");
    scanf("%d", &loginOk);

    printf("Dispositivo conhecido? (1/0): ");
    scanf("%d", &dispositivoConhecido);

    printf("Tentativa suspeita? (1/0): ");
    scanf("%d", &tentativaSuspeita);

    // Implementação da lógica
    if (loginOk == 1) {
        // Se o login está ok, verifica a segurança do dispositivo e comportamento
        if (dispositivoConhecido == 1 && tentativaSuspeita == 0) {
            printf("ACESSO LIBERADO\n");
        } else {
            printf("VERIFICACAO EXTRA NECESSARIA\n");
        }
    } else {
        // Se o login estiver errado, nem checa o resto
        printf("ACESSO NEGADO\n");
    }

    return 0;
}