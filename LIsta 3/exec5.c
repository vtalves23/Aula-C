#include <stdio.h>

int main() {
    int idade, genero, acompanhado;

    printf("Digite a idade: ");
    scanf("%d", &idade);

    printf("Digite o genero preferido (1-acao, 2-comedia, 3-terror): ");
    scanf("%d", &genero);

    printf("Esta acompanhado? (1/0): ");
    scanf("%d", &acompanhado);

    // Implementação da lógica do sistema de recomendação
    if (idade < 18) {
        // Bloco Menor de Idade: Bloqueio estrito de terror (gênero 3)
        if (genero == 3) {
            printf("TERROR NAO RECOMENDADO\n");
        } else {
            printf("RECOMENDAR NORMALMENTE\n");
        }
    } 
    else {
        // Bloco Maior de Idade: Avalia se está sozinho assistindo terror
        if (genero == 3 && acompanhado == 0) {
            printf("RECOMENDAR COM AVISO\n");
        } else {
            printf("RECOMENDAR NORMALMENTE\n");
        }
    }

    return 0;
}