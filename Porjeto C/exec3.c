p,q,p && q
V,V,V
V,F,F
F,V,F
F,F,F

#include <stdio.h>

int main() {
    float consumos[7];
    int horarioPico;
    int i;

    int altoCusto = 0;
    int custoNormal = 0;

    float soma = 0;
    float media;

    // Loop para ler e processar os dados dos 7 equipamentos
    for(i = 0; i < 7; i++) {
        printf("--- Equipamento %d ---\n", i + 1);
        
        // 1. Ler os consumos e armazenar no vetor consumos
        printf("Digite o consumo (em kWh): ");
        scanf("%f", &consumos[i]);
        
        // 2. Ler se cada equipamento está em horário de pico (1-Sim / 0-Não)
        printf("Esta em horario de pico? (1-Sim / 0-Nao): ");
        scanf("%d", &horarioPico);

        // 3. Usar if com AND (&&) para classificar o custo e 4. Contar as ocorrências
        if (consumos[i] > 100.0 && horarioPico == 1) {
            printf("Status: ALTO CUSTO\n\n");
            altoCusto++; // Incrementa quantidade de equipamentos de alto custo
        } else {
            printf("Status: CUSTO NORMAL\n\n");
            custoNormal++; // Incrementa quantidade de custo normal
        }

        // Acumula o consumo atual para o cálculo da média posterior
        soma += consumos[i];
    }

    // 5. Calcular a média dos consumos (Soma total dividida por 7 aparelhos)
    media = soma / 7.0;

    // Exibição dos resultados finais
    printf("=================================\n");
    printf("       RELATÓRIO DE CONSUMO      \n");
    printf("=================================\n");
    printf("Quantidade de equipamentos com alto custo: %d\n", altoCusto);
    printf("Quantidade de equipamentos com custo normal: %d\n", custoNormal);
    printf("Consumo medio dos equipamentos: %.2f kWh\n", media);

    return 0;
}