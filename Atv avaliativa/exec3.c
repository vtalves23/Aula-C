p,q,p && q
V,V,V
V,F,F
F,V,F
F,F,F


#include <stdio.h>

int main() {
    float temperaturas[7];
    int i;

    int seguras = 0;
    int foraFaixa = 0;

    float soma = 0;
    float media;

    // Loop para ler e processar as 7 temperaturas
    for(i = 0; i < 7; i++) {
        printf("Digite a temperatura %d (em °C): ", i + 1);
        // 1. Ler as 7 temperaturas e armazenar no vetor temperaturas
        scanf("%f", &temperaturas[i]);

        // 2. Usar if com AND (&&) para verificar a faixa segura
        if (temperaturas[i] >= 20.0 && temperaturas[i] <= 30.0) {
            printf("Status: TEMPERATURA SEGURA\n\n");
            // 3. Contar temperaturas seguras
            seguras++;
        } else {
            printf("Status: TEMPERATURA FORA DA FAIXA\n\n");
            // 3. Contar temperaturas fora da faixa
            foraFaixa++;
        }

        // Acumula a temperatura atual para o cálculo da média
        soma += temperaturas[i];
    }

    // 4. Calcular a média (total da soma dividido por 7 dias/registros)
    media = soma / 7.0;

    // Exibição dos resultados finais
    printf("=================================\n");
    printf("      RELATÓRIO DE TEMPERATURAS  \n");
    printf("=================================\n");
    printf("Quantidade de temperaturas seguras: %d\n", seguras);
    printf("Quantidade de temperaturas fora da faixa: %d\n", foraFaixa);
    printf("Média das temperaturas: %.1f°C\n", media);

    return 0;
}