#include <stdio.h>

int main() {
    float compra;
    
    printf ("digite o valor da compra: ");
    scanf ("%f", &compra);
    
    if (compra >= 100) {
        printf ("recebe desconto\n");
    } else {
        printf ("nao recebe desconto\n");
    }

    return 0;
}
