#include <stdio.h>

int main() {
    int idade;

    printf("Digite a idade: ");
    scanf("%d", &idade);

    if (idade >= 18) {
        printf("PODE ENTRAR\n");
    } else if (idade >= 16) {
        printf("PODE ENTRAR COM RESPONSAVEL\n");
    } else {
        printf("NAO PODE ENTRAR\n");
    }

    return 0;
}