#include <stdio.h>

int main() {
    int idade;

    printf("Digite a idade: ");
    scanf("%d", &idade);

    if (idade >= 60) {
        printf("IDOSO\n");
    } else if (idade >= 18) {
        printf("ADULTO\n");
    } else {
        printf("MENOR\n");
    }

    return 0;
}