def ler_float(mensagem: str, minimo: float = 0.0, estritamente_maior: bool = False) -> float:
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if estritamente_maior and valor <= minimo:
                print(f"Erro: informe um valor maior que {minimo}.")
                continue
            if not estritamente_maior and valor < minimo:
                print(f"Erro: informe um valor maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: digite um número válido.")


def diagnosticar_financas_familiares() -> None:
    print("=== DIAGNÓSTICO FINANCEIRO FAMILIAR ===")
    renda = ler_float("Renda mensal familiar (R$): ", minimo=0.0, estritamente_maior=True)
    moradia = ler_float("Gastos com moradia (R$): ", minimo=0.0)
    alimentacao = ler_float("Gastos com alimentação (R$): ", minimo=0.0)
    transporte = ler_float("Gastos com transporte (R$): ", minimo=0.0)
    saude = ler_float("Gastos com saúde (R$): ", minimo=0.0)
    educacao = ler_float("Gastos com educação (R$): ", minimo=0.0)
    lazer = ler_float("Gastos com lazer (R$): ", minimo=0.0)
    dividas = ler_float("Gastos com dívidas no mês (R$): ", minimo=0.0)

    total_despesas = moradia + alimentacao + transporte + saude + educacao + lazer + dividas
    saldo_mensal = renda - total_despesas
    perc_comprometida = (total_despesas / renda) * 100.0
    perc_dividas = (dividas / renda) * 100.0

    # Classificação combinando saldo mensal, percentual total comprometido e percentual de dívidas
    if total_despesas > renda and saldo_mensal < -0.20 * renda:
        situacao = "Insolvência"
        recomendacoes = [
            "Priorize a sobrevivência financeira imediata: corte todos os gastos não essenciais (como lazer) e revise itens variáveis.",
            "Negocie ou suspenda temporariamente cobranças de dívidas com credores e busque orientação financeira ou jurídica se necessário.",
            "Evite contrair novos empréstimos ou parcelamentos que aumentem o déficit mensal."
        ]
    elif perc_comprometida > 85.0 or perc_dividas > 35.0:
        situacao = "Crítica"
        recomendacoes = [
            "Reduza imediatamente despesas discricionárias e estabeleça um teto rígido para cada categoria.",
            "Liste todas as dívidas por taxa de juros e priorize a quitação ou portabilidade das mais caras.",
            "Busque fontes de renda extra temporária para acelerar o reequilíbrio do orçamento."
        ]
    elif 70.0 < perc_comprometida <= 85.0 or (20.0 < perc_dividas <= 35.0 and saldo_mensal >= 0):
        situacao = "Atenção"
        recomendacoes = [
            "Monitore de perto os gastos variáveis (alimentação, transporte e lazer) para não ultrapassar o orçamento.",
            "Evite assumir novas parcelas até reduzir o peso das dívidas para até 20% da renda.",
            "Direcione parte do saldo positivo mensal para formar ou reforçar a reserva de emergência."
        ]
    else:
        situacao = "Saudável"
        recomendacoes = [
            "Mantenha o controle mensal e o nível contido de endividamento.",
            "Destine o superávit mensal para construir ou ampliar a reserva de emergência (6 a 12 meses de despesas).",
            "Invista o excedente de acordo com seus objetivos de curto, médio e longo prazo."
        ]

    print("\n--- DIAGNÓSTICO FINANCEIRO ---")
    print(f"Renda mensal: R$ {renda:,.2f}")
    print(f"Total de despesas: R$ {total_despesas:,.2f}")
    print(f"Saldo mensal: R$ {saldo_mensal:,.2f}")
    print(f"Percentual da renda comprometida: {perc_comprometida:.2f}%")
    print(f"Percentual gasto com dívidas: {perc_dividas:.2f}%")
    print(f"Classificação da situação: {situacao}")
    print("\nRecomendações:")
    for item in recomendacoes:
        print(f"  • {item}")


if __name__ == "__main__":
    diagnosticar_financas_familiares()
