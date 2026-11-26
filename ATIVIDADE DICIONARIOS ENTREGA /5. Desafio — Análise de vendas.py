def formatar_brl(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def analise_vendas() -> None:
    vendas: dict[str, int | float] = {
        "Janeiro": 12500,
        "Fevereiro": 9800,
        "Março": 15300,
        "Abril": 11700,
        "Maio": 18400,
    }

    # 1. Valor total vendido e 2. Média mensal de vendas
    total_vendido = float(sum(vendas.values()))
    media_mensal = total_vendido / len(vendas)

    # 3. Mês com maior venda e 4. Mês com menor venda
    mes_maior = max(vendas, key=lambda m: vendas[m])
    mes_menor = min(vendas, key=lambda m: vendas[m])

    # 5. Meses que tiveram vendas acima da média + Desafio adicional (dictionary comprehension)
    acima_da_media: dict[str, int | float] = {
        mes: valor for mes, valor in vendas.items() if valor > media_mensal
    }

    print(f"Total vendido: {formatar_brl(total_vendido)}")
    print(f"Média mensal: {formatar_brl(media_mensal)}")
    print(f"Maior venda: {mes_maior} - {formatar_brl(float(vendas[mes_maior]))}")
    print(f"Menor venda: {mes_menor} - {formatar_brl(float(vendas[mes_menor]))}")
    print("\nMeses acima da média:")
    for mes in acima_da_media:
        print(mes)

    print("\nDicionário acima_da_media:", acima_da_media)


if __name__ == "__main__":
    analise_vendas()
