#include <stdio.h>

int main() {
    float meta, valorMes, total = 0;
    int mesesValidos = 0;
    
    printf("Digite a meta de economia: ");
    scanf("%f", &meta);
    
    while (total < meta) {
        printf("Digite o valor economizado no mes: ");
        scanf("%f", &valorMes);
        
        if (valorMes > 0) {
            total += valorMes;        
            mesesValidos++;           
        } else {
            printf("VALOR DESCONSIDERADO\n");
        }
    }
    
    printf("Total economizado: %.2f\n", total);
    printf("Meses validos: %d\n", mesesValidos);

    return 0;
}