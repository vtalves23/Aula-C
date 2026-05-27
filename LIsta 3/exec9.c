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

    // Implementação da lógica de aprovação de corrida
    if (motoristaDisponivel == 1) {
        // Camada Interna: Existe motorista, agora avalia se a corrida vale a pena
        // Regra: Curta distância (<= 10) OU bom retorno financeiro (>= 30)
        if (distancia <= 10.0 || valor >= 30.0) {
            printf("CORRIDA ACEITA\n");
        } else {
            // Se for longe E pagar pouco, o motorista recusa
            printf("CORRIDA RECUSADA POR BAIXA RENTABILIDADE\n");
        }
    } 
    else {
        // Camada Externa: Não há nenhum motorista disponível na região
        printf("SEM MOTORISTAS DISPONIVEIS\n");
    }

    return 0;
}