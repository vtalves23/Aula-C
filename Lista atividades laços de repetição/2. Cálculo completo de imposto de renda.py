DEDUCAO_POR_DEPENDENTE = 250.0


def ler_float(mensagem: str, minimo: float = 0.0) -> float:
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < minimo:
                print(f"Erro: informe um valor maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: digite um número válido.")


def ler_int(mensagem: str, minimo: int = 0) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"Erro: informe um número inteiro maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def calcular_ir() -> None:
    print("=== CÁLCULO COMPLETO DE IMPOSTO DE RENDA ===")
    salario_bruto = ler_float("Salário bruto (R$): ", minimo=0.0)
    num_dependentes = ler_int("Quantidade de dependentes: ", minimo=0)
    previdencia = ler_float("Valor pago em previdência (R$): ", minimo=0.0)
    pensao = ler_float("Valor pago em pensão alimentícia (R$): ", minimo=0.0)

    deducao_dependentes = num_dependentes * DEDUCAO_POR_DEPENDENTE
    total_deducoes = previdencia + pensao + deducao_dependentes
    base_calculo_bruta = salario_bruto - total_deducoes

    deducoes_maiores_que_salario = total_deducoes > salario_bruto
    base_calculo = max(0.0, base_calculo_bruta)

    if base_calculo <= 2500.0:
        aliquota = 0.0
        faixa_texto = "Isento (0%)"
    elif base_calculo <= 3500.0:
        aliquota = 0.075
        faixa_texto = "7,5%"
    elif base_calculo <= 5000.0:
        aliquota = 0.15
        faixa_texto = "15%"
    elif base_calculo <= 7500.0:
        aliquota = 0.225
        faixa_texto = "22,5%"
    else:
        aliquota = 0.275
        faixa_texto = "27,5%"

    imposto = base_calculo * aliquota
    salario_liquido = salario_bruto - imposto

    print("\n--- DEMONSTRATIVO DE IMPOSTO DE RENDA ---")
    if deducoes_maiores_que_salario:
        print(
            f"Aviso: o total de deduções (R$ {total_deducoes:,.2f}) excede o salário bruto "
            f"(R$ {salario_bruto:,.2f}). A base de cálculo foi ajustada para R$ 0,00."
        )
    print(f"Salário bruto: R$ {salario_bruto:,.2f}")
    print(f"Total de deduções: R$ {total_deducoes:,.2f}")
    print(f"Base de cálculo: R$ {base_calculo:,.2f}")
    print(f"Alíquota: {faixa_texto}")
    print(f"Imposto: R$ {imposto:,.2f}")
    print(f"Salário líquido: R$ {salario_liquido:,.2f}")


if __name__ == "__main__":
    calcular_ir()
