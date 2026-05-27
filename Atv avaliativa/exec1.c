p,q,p && q
V,V,V
V,F,F
F,V,F
F,F,F

#include <stdio.h>

int main() {
    float notas[8];
    float frequencia;
    int i;

    int aprovados = 0;
    int reprovados = 0;

    float maiorNota = 0;

    // Loop para ler os dados dos 8 participantes
    for(i = 0; i < 8; i++) {
        printf("--- Participante %d ---\n", i + 1);
        
        // 1. Ler a nota e armazenar no vetor
        printf("Digite a nota (0 a 10): ");
        scanf("%f", &notas[i]);
        
        // 2. Ler a frequência do participante
        printf("Digite a frequencia (0 a 100): ");
        scanf("%f", &frequencia);

        // 3. Usar if com AND (&&) para classificar e 4. Contar aprovados/reprovados
        if (notas[i] >= 7.0 && frequencia >= 75.0) {
            printf("Status: APROVADO\n\n");
            aprovados++; // Incrementa aprovados
        } else {
            printf("Status: REPROVADO\n\n");
            reprovados++; // Incrementa reprovados
        }

        // 5. Descobrir a maior nota
        // Se for o primeiro loop ou se a nota atual for maior que a maior guardada
        if (i == 0 || notas[i] > maiorNota) {
            maiorNota = notas[i];
        }
    }

    // Exibição dos resultados finais
    printf("=================================\n");
    printf("         RESUMO FINAL            \n");
    printf("=================================\n");
    printf("Quantidade de aprovados: %d\n", aprovados);
    printf("Quantidade de reprovados: %d\n", reprovados);
    printf("Maior nota registrada: %.2f\n", maiorNota);

    return 0;
}