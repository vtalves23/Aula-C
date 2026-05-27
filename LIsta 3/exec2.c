#include <stdio.h>

int main() {
    int tipoUsuario, horario, autorizacao;

    printf("Digite o tipo de usuario (1-aluno, 2-professor): ");
    scanf("%d", &tipoUsuario);

    printf("Digite o horario atual: ");
    scanf("%d", &horario);

    printf("Digite a autorizacao especial (1/0): ");
    scanf("%d", &autorizacao);

    // Implementação da lógica de acesso
    if (tipoUsuario == 2) {
        // Regra do Professor: Entrada sempre permitida
        printf("ENTRADA PERMITIDA\n");
    } 
    else if (tipoUsuario == 1) {
        // Regra do Aluno: Verificar horário ou autorização especial
        if (horario >= 8 && horario <= 18) {
            // Horário regular (8h às 18h)
            printf("ENTRADA PERMITIDA\n");
        } else if (autorizacao == 1) {
            // Fora do horário regular, mas tem autorização
            printf("ENTRADA PERMITIDA\n");
        } else {
            // Fora do horário e sem autorização
            printf("ENTRADA NEGADA\n");
        }
    } 
    else {
        // Caso seja digitado um tipo de usuário inválido (ex: 3, 0, etc.)
        printf("ENTRADA NEGADA\n");
    }

    return 0;
}