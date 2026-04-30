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

    // Lógica principal
    if (premium == 1 && distancia <= 20) {
        printf("ENTREGA GRATUITA\n");
    } 
    else {
        // Bloco para clientes não premium ou premium com distância > 20
        if (distancia <= 10 && chuva == 0) {
            printf("ENTREGA NORMAL\n");
        } 
        else {
            printf("ENTREGA COM TAXA\n");
        }
    }

    return 0;
}