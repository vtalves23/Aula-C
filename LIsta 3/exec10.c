#include <stdio.h>

int main() {
    float cpu, memoria;
    int erroCritico;

    printf("Digite o uso de CPU: ");
    scanf("%f", &cpu);

    printf("Digite o uso de memoria: ");
    scanf("%f", &memoria);

    printf("Ha erro critico? (1/0): ");
    scanf("%d", &erroCritico);

    // Implementação da lógica de alerta do servidor
    if (erroCritico == 1) {
        // Prioridade Absoluta: Se há erro crítico, o estado é o mais grave
        printf("ALERTA MAXIMO\n");
    } 
    else {
        // Sem erro crítico: Avalia o consumo de hardware por faixas de risco
        
        if (cpu > 80.0 && memoria > 80.0) {
            // Cenário Crítico: Ambos estão sobrecarregados (> 80)
            printf("ALERTA ALTO\n");
        } 
        else if (cpu > 80.0 || memoria > 80.0) {
            // Cenário de Atenção: Apenas UM dos dois passou de 80
            printf("ALERTA MEDIO\n");
        } 
        else {
            // Cenário Ideal: Ambos estão trabalhando abaixo ou igual a 80
            printf("FUNCIONAMENTO NORMAL\n");
        }
    }

    return 0;
}