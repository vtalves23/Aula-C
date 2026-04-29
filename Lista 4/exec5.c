#include <stdio.h>

int main() {
    int i, numero ,total = 0, positivos = 0;
    printf ("informe o número:\n");
    while (numero != 0) {
        total++;
        if (numero > 0){
            positivos++;
        }
        printf ("informe o número:\n");
        scanf ("%d", &numero);
  
}
printf("Total: %d\n", total);
printf("Positivos: %d\n", positivos);
    return 0;
}