#include <stdio.h>

int main() {
    float distancia, valor;
    int motoristaDisponivel;

    printf("Digite a distancia da corrida: ");
    scanf("%f", &distancia);

    printf("Digite o valor estimado: ");
    scanf("%f", &valor);

    printf("Motorista disponivel? (1/0): ");
    scanf("%d", &motoristaDisponivel);

    if (motoristaDisponivel == 1) {
        
        if (distancia <= 10 || valor >= 30) {
            printf("CORRIDA ACEITA\n");
        } else {
            printf("CORRIDA RECUSADA POR BAIXA RENTABILIDADE\n");
        }
    } else {
        printf("SEM MOTORISTAS DISPONIVEIS\n");
    }
    return 0;
}