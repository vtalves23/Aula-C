// Peça a senha até o usuário acertar (1234).

#include <stdio.h>

int main() {
    int senha;

    scanf("%d", &senha);

    while (senha != 1234) {
        scanf("%d", &senha);
    }

    printf("ACESSO LIBERADO\n");

    return 0;
}