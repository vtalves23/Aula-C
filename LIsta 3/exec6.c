#include <stdio.h>

int main() {
    int codigoValido, jaUsouCupom;
    float valorCompra;

    printf("Codigo valido? (1/0): ");
    scanf("%d", &codigoValido);

    printf("Digite o valor da compra: ");
    scanf("%f", &valorCompra);

    printf("Ja usou cupom? (1/0): ");
    scanf("%d", &jaUsouCupom);

    // Implementação da validação do cupom em camadas
    if (codigoValido == 1) {
        // Camada Interna: O código existe, agora valida as regras de uso
        if (jaUsouCupom == 0 && valorCompra >= 100.0) {
            // Cliente novo para este cupom E atingiu o valor mínimo de R$ 100
            printf("DESCONTO APLICADO\n");
        } else {
            // O código é real, mas o cliente já usou OU a compra ficou abaixo de 100
            printf("CUPOM INVALIDO PARA USO\n");
        }
    } 
    else {
        // Camada Externa: O código digitado sequer é válido/existe
        printf("CUPOM INVALIDO\n");
    }

    return 0;
}