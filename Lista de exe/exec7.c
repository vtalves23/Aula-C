#include <stdio.h>

int main() {
    float consumo;
    int horarioPico, energiaSolar;

    printf("Digite o consumo atual: ");
    scanf("%f", &consumo);

    printf("Horario de pico? (1/0): ");
    scanf("%d", &horarioPico);

    printf("Possui energia solar? (1/0): ");
    scanf("%d", &energiaSolar);

    
    if (horarioPico == 1) {
       
        if (consumo > 0 && energiaSolar == 0) {
            printf("ALERTA DE ALTO CONSUMO\n");
        } else {
            printf("CONSUMO CONTROLADO\n");
        }
    } 
    else {
      
        if (consumo > 500) {
            printf("ALERTA DE CONSUMO\n");
        } else {
            printf("CONSUMO NORMAL\n");
        }
    }