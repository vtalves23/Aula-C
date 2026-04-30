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

    if (erroCritico == 1) {
        printf("ALERTA MAXIMO\n");
    } 
    else {
        
        if (cpu > 80 && memoria > 80) {
            printf("ALERTA ALTO\n");
        } 
        
        else if (cpu > 80 || memoria > 80) {
            printf("ALERTA MEDIO\n");
        } 
      
        else {
            printf("FUNCIONAMENTO NORMAL\n");
        }
    }

    return 0;
}