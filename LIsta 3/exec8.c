#include <stdio.h>

int main() {
    int pessoas, reserva, horario;

    printf("Digite o numero de pessoas: ");
    scanf("%d", &pessoas);

    printf("Tem reserva? (1/0): ");
    scanf("%d", &reserva);

    printf("Digite o horario atual: ");
    scanf("%d", &horario);

    // Implementação da lógica de atendimento
    if (reserva == 1) {
        // Regra de Ouro: Quem tem reserva sempre tem atendimento imediato
        printf("ATENDIMENTO IMEDIATO\n");
    } 
    else {
        // Caso Contrário: Não tem reserva. Vamos analisar o horário.
        
        // Verifica se está no horário de pico do Almoço (12h às 14h) OU do Jantar (19h às 21h)
        if ((horario >= 12 && horario <= 14) || (horario >= 19 && horario <= 21)) {
            
            // Dentro do horário de pico, o tamanho do grupo decide a espera
            if (pessoas <= 4) {
                printf("ESPERA CURTA\n");
            } else {
                printf("ESPERA LONGA\n");
            }
            
        } else {
            // Fora dos horários de pico, mesmo sem reserva o atendimento é rápido
            printf("ATENDIMENTO IMEDIATO\n");
        }
    }

    return 0;
}