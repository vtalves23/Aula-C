#include <stdio.h>

int main() {
    int codigo;
    
    printf ("Digite o codigo de acesso: ");
    scanf ("%d", &codigo);
    while (codigo != 4321) {
        printf ("CODIGO INCORRETO. \n");
        printf ("Insira o codigo novamente: ");
        scanf ("%d", &codigo);
    }
    printf ("ACESSO LIBERADO");
    return 0;
}