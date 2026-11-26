def ler_float(mensagem: str, minimo: float | None = None, estritamente_maior: bool = False) -> float:
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if minimo is not None:
                if estritamente_maior and valor <= minimo:
                    print(f"Erro: informe um valor maior que {minimo}.")
                    continue
                if not estritamente_maior and valor < minimo:
                    print(f"Erro: informe um valor maior ou igual a {minimo}.")
                    continue
            return valor
        except ValueError:
            print("Erro: digite um número válido.")


def ler_int(mensagem: str, minimo: int | None = None, estritamente_maior: bool = False) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None:
                if estritamente_maior and valor <= minimo:
                    print(f"Erro: informe um inteiro maior que {minimo}.")
                    continue
                if not estritamente_maior and valor < minimo:
                    print(f"Erro: informe um inteiro maior ou igual a {minimo}.")
                    continue
            return valor
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def analisar_credito() -> None:
    print("=== SISTEMA DE CLASSIFICAÇÃO DE CRÉDITO ===")
    idade = ler_int("Idade: ", minimo=0)
    salario = ler_float("Salário mensal (R$): ", minimo=0, estritamente_maior=True)
    divida_atual = ler_float("Valor da dívida atual (R$): ", minimo=0)
    tempo_emprego = ler_int("Tempo de emprego (em meses): ", minimo=0)
    valor_solicitado = ler_float("Valor solicitado (R$): ", minimo=0, estritamente_maior=True)
    num_parcelas = ler_int("Número de parcelas: ", minimo=0, estritamente_maior=True)

    comprometimento_atual = divida_atual / salario
    valor_parcela = valor_solicitado / num_parcelas
    percentual_nova_parcela = valor_parcela / salario
    novo_comprometimento = comprometimento_atual + percentual_nova_parcela

    idade_ok = 21 <= idade <= 65
    salario_ok = salario >= 2500.0
    emprego_aprovado_ok = tempo_emprego >= 12
    emprego_restricao_ok = tempo_emprego >= 6
    comp_atual_ok = comprometimento_atual <= 0.30
    nova_parcela_ok = percentual_nova_parcela <= 0.25
    soma_restricao_ok = novo_comprometimento <= 0.50

    motivo_reprovacao = None

    if idade_ok and salario_ok and emprego_aprovado_ok and comp_atual_ok and nova_parcela_ok:
        resultado = "Aprovada"
    elif idade_ok and salario_ok and emprego_restricao_ok and soma_restricao_ok:
        resultado = "Aprovada com restrições"
    else:
        resultado = "Reprovada"
        # Identifica o motivo principal de reprovação na ordem de prioridade
        if not idade_ok:
            motivo_reprovacao = "Idade fora da faixa permitida (deve estar entre 21 e 65 anos)."
        elif not salario_ok:
            motivo_reprovacao = "Salário mensal inferior ao mínimo exigido de R$ 2.500,00."
        elif not emprego_restricao_ok:
            motivo_reprovacao = "Tempo de emprego inferior a 6 meses."
        elif not soma_restricao_ok:
            motivo_reprovacao = (
                f"Comprometimento total ({novo_comprometimento * 100:.2f}%) ultrapassa o limite de 50% do salário."
            )
        elif not emprego_aprovado_ok:
            motivo_reprovacao = "Tempo de emprego inferior a 12 meses para aprovação plena."
        elif not comp_atual_ok:
            motivo_reprovacao = f"Comprometimento atual ({comprometimento_atual * 100:.2f}%) acima de 30%."
        elif not nova_parcela_ok:
            motivo_reprovacao = (
                f"Nova parcela ({percentual_nova_parcela * 100:.2f}% do salário) acima do limite de 25%."
            )

    print("\n--- RESULTADO DA ANÁLISE DE CRÉDITO ---")
    print(f"Valor da parcela: R$ {valor_parcela:,.2f}")
    print(f"Percentual atual de comprometimento: {comprometimento_atual * 100:.2f}%")
    print(f"Novo percentual de comprometimento: {novo_comprometimento * 100:.2f}%")
    print(f"Resultado da análise: {resultado}")
    if motivo_reprovacao:
        print(f"Motivo principal da reprovação: {motivo_reprovacao}")


if __name__ == "__main__":
    analisar_credito()
