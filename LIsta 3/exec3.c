#include <stdio.h>

int main() {
    float distancia;
    int premium, chuva;

    printf("Digite a distancia da entrega: ");
    scanf("%f", &distancia);

    printf("Cliente premium? (1/0): ");
    scanf("%d", &premium);

    printf("Esta chovendo? (1/0): ");
    scanf("%d", &chuva);

    // Implementação da lógica de entrega inteligente
    if (premium == 1 && distancia <= 20.0) {
        // Regra Especial: Cliente Premium dentro do limite de distância
        printf("ENTREGA GRATUITA\n");
    } 
    else {
        // "Caso contrário": Entra aqui se NÃO for premium OU se for premium mas a distância for > 20
        if (distancia <= 10.0 && chuva == 0) {
            // Curta distância e sem chuva
            printf("ENTREGA NORMAL\n");
        } else {
            // Longa distância OU está chovendo
            printf("ENTREGA COM TAXA\n");
        }
    }

    return 0;
}