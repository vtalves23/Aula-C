#include <stdio.h>

int main() {
    float nota;
    
    printf ("digite a nota: ");
    scanf ("%f", &nota);
    
    if (nota >= 7) {
        printf ("aprovado\n");
    } else if (nota >= 5) {
        printf ("recuperacao\n");
    } else {
        printf ("reprovado\n");
    }

    return 0;
}
