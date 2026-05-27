#include <stdio.h>
int main() {
    int numeros[8];
    int pos, soma;
    for (pos = 0; pos < 8; pos++){
        printf("Digite o número da posição %d: ", pos);
        scanf("%d", &numeros[pos]);
    }
    for (pos = 0; pos < 8; pos++){
        soma += numeros[pos]; //soma = soma + numeros[pos]
    }
    printf("A soma foi igual a %d ", soma);
    return 0;
}