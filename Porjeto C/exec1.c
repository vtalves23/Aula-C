p,q,p && q
V,V,V
V,F,F
F,V,F
F,F,F

#include <stdio.h>

int main() {
    int quantidades[8];
    int essencial;
    int i;

    int urgente = 0;
    int estoqueOk = 0;

    // Inicializamos com 0, mas trataremos o primeiro valor no loop
    int menorQuantidade = 0; 

    // Loop para ler e processar os 8 produtos
    for(i = 0; i < 8; i++) {
        printf("--- Produto %d ---\n", i + 1);
        
        // 1. Ler a quantidade e armazenar no vetor quantidades
        printf("Digite a quantidade em estoque: ");
        scanf("%d", &quantidades[i]);
        
        // 2. Ler se o produto é essencial (1 para sim, 0 para não)
        printf("O produto eh essencial? (1-Sim / 0-Nao): ");
        scanf("%d", &essencial);

        // 3. Usar if com AND (&&) para classificar e 4. Contar produtos
        if (quantidades[i] < 10 && essencial == 1) {
            printf("Status: REPOSICAO URGENTE\n\n");
            urgente++; // Incrementa a quantidade de alertas urgentes
        } else {
            printf("Status: ESTOQUE OK\n\n");
            estoqueOk++; // Incrementa a quantidade de estoques estáveis
        }

        // 5. Descobrir a menor quantidade registrada
        // Se for o primeiro produto (i == 0) ou se a quantidade atual for menor que a menor salva
        if (i == 0 || quantidades[i] < menorQuantidade) {
            menorQuantidade = quantidades[i];
        }
    }

    // Exibição dos resultados finais exigidos
    printf("=================================\n");
    printf("        RELATÓRIO DE ESTOQUE     \n");
    printf("=================================\n");
    printf("Quantidade de produtos com reposicao urgente: %d\n", urgente);
    printf("Quantidade de produtos com estoque ok: %d\n", estoqueOk);
    printf("Menor quantidade registrada: %d\n", menorQuantidade);

    return 0;
}