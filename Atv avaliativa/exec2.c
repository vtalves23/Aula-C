p,q,p || q
V,V,V
V,F,V
F,V,V
F,F,F


#include <stdio.h>

int main() {
    float vendas[10];
    int vendaEspecial;
    int i;

    float totalVendido = 0;
    int destaque = 0;
    int comum = 0;

    // Loop para ler e processar as 10 vendas
    for(i = 0; i < 10; i++) {
        printf("--- Venda %d ---\n", i + 1);
        
        // 1. Ler o valor da venda e armazenar no vetor
        printf("Digite o valor da venda: R$ ");
        scanf("%f", &vendas[i]);
        
        // 2. Ler se a venda foi especial (1 para sim, 0 para não)
        printf("A venda foi especial? (1-Sim / 0-Nao): ");
        scanf("%d", &vendaEspecial);

        // 3. Usar if com OR (||) para classificar
        if (vendas[i] >= 100.0 || vendaEspecial == 1) {
            printf("Status: VENDA COM DESTAQUE\n\n");
            // 5. Contar vendas com destaque
            destaque++; 
        } else {
            printf("Status: VENDA COMUM\n\n");
            // 5. Contar vendas comuns
            comum++; 
        }

        // 4. Somar o valor ao total vendido
        totalVendido += vendas[i];
    }

    // Exibição dos resultados finais
    printf("=================================\n");
    printf("         RESUMO DAS VENDAS       \n");
    printf("=================================\n");
    printf("Total vendido: R$ %.2f\n", totalVendido);
    printf("Quantidade de vendas com destaque: %d\n", destaque);
    printf("Quantidade de vendas comuns: %d\n", comum);

    return 0;
}