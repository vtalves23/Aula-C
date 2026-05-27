p,q,p || q
V,V,V
V,F,V
F,V,V
F,F,F


#include <stdio.h>

int main() {
    int idades[10];
    int convite;
    int i;

    int permitidas = 0;
    int negadas = 0;

    int maiorIdade = 0;

    // Loop para ler e processar os dados das 10 pessoas
    for(i = 0; i < 10; i++) {
        printf("--- Pessoa %d ---\n", i + 1);
        
        // 1. Ler a idade e armazenar no vetor idades
        printf("Digite a idade: ");
        scanf("%d", &idades[i]);
        
        // 2. Ler se a pessoa possui convite (1 para sim, 0 para não)
        printf("Possui convite? (1-Sim / 0-Nao): ");
        scanf("%d", &convite);

        // 3. Usar if com OR (||) para classificar e 4. Contar as entradas
        if (idades[i] >= 18 || convite == 1) {
            printf("Status: ENTRADA PERMITIDA\n\n");
            permitidas++; // Incrementa quantidade de permitidas
        } else {
            printf("Status: ENTRADA NEGADA\n\n");
            negadas++; // Incrementa quantidade de negadas
        }

        // 5. Descobrir a maior idade registrada
        // Se for a primeira pessoa (i == 0) ou se a idade atual for maior que a maior salva
        if (i == 0 || idades[i] > maiorIdade) {
            maiorIdade = idades[i];
        }
    }

    // Exibição dos resultados finais
    printf("=================================\n");
    printf("         RESUMO DO EVENTO        \n");
    printf("=================================\n");
    printf("Quantidade de entradas permitidas: %d\n", permitidas);
    printf("Quantidade de entradas negadas: %d\n", negadas);
    printf("Maior idade registrada: %d anos\n", maiorIdade);

    return 0;
}