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


def ler_int(mensagem: str, minimo: int = 1) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"Erro: informe um inteiro maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def gerar_relatorio_parcelas() -> None:
    print("=== GERADOR DE RELATÓRIO DE PARCELAS (JUROS SIMPLES) ===")
    valor_compra = ler_float("Valor da compra (R$): ", minimo=0.0, estritamente_maior=True)
    max_parcelas = ler_int("Quantidade máxima de parcelas: ", minimo=1)
    taxa_mensal = ler_float("Taxa de juros mensal (%): ", minimo=0.0) / 100.0
    limite_parcela = ler_float("Limite máximo desejado para o valor da parcela (R$): ", minimo=0.0, estritamente_maior=True)

    print("\n--- RELATÓRIO DE OPÇÕES DE PARCELAMENTO ---")
    opcoes_abaixo_limite = ""

    for n in range(1, max_parcelas + 1):
        juros = valor_compra * taxa_mensal * n
        total_com_juros = valor_compra + juros
        valor_parcela = total_com_juros / n

        print(
            f"{n}x de R$ {valor_parcela:,.2f} — Total: R$ {total_com_juros:,.2f} "
            f"(Juros: R$ {juros:,.2f})"
        )

        if valor_parcela < limite_parcela:
            if opcoes_abaixo_limite:
                opcoes_abaixo_limite += ", "
            opcoes_abaixo_limite += f"{n}x (R$ {valor_parcela:,.2f})"

    print("\n--- ANÁLISE DO LIMITE DE PARCELA ---")
    if opcoes_abaixo_limite:
        print(f"Opções com parcela inferior a R$ {limite_parcela:,.2f}: {opcoes_abaixo_limite}")
    else:
        print(f"Nenhuma opção de 1x a {max_parcelas}x possui parcela inferior a R$ {limite_parcela:,.2f}.")


if __name__ == "__main__":
    gerar_relatorio_parcelas()
