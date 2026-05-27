#include <stdio.h>

int main() {
    int loginOk, dispositivoConhecido, tentativaSuspeita;

    printf("Login correto? (1/0): ");
    scanf("%d", &loginOk);

    printf("Dispositivo conhecido? (1/0): ");
    scanf("%d", &dispositivoConhecido);

    printf("Tentativa suspeita? (1/0): ");
    scanf("%d", &tentativaSuspeita);

    // Implementação da verificação de segurança bancária
    if (loginOk == 1) {
        // Camada Interna: O login está correto, agora avalia o risco
        if (dispositivoConhecido == 1 && tentativaSuspeita == 0) {
            // Cenário seguro: Dispositivo confiável E nenhuma atividade suspeita
            printf("ACESSO LIBERADO\n");
        } else {
            // Cenário de risco: Dispositivo novo OU comportamento suspeito detectado
            printf("VERIFICACAO EXTRA NECESSARIA\n");
        }
    } 
    else {
        // Camada Externa: O login falhou
        printf("ACESSO NEGADO\n");
    }

    return 0;
}