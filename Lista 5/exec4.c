#include <stdio.h>

int main() {
    int i, status;
    int concluidas = 0, pendentes = 0;
    
    for (i = 1; i <= 8; i++){
        printf ("Digite a opção %d°(1=Sim/0=Não):", i);
        scanf ("%d", &status);
        
        if (status == 1){
            concluidas++;
        }else {
            pendentes++;
        }
    }
    
    printf ("Concluidas: %d\n", concluidas);
    printf ("Pendentes: %d\n", pendentes);
    return 0;
}