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


def simular_financiamento() -> None:
    print("=== SIMULAÇÃO DE FINANCIAMENTO ===")
    saldo = ler_float("Valor financiado (R$): ", minimo=0.0, estritamente_maior=True)
    taxa_perc = ler_float("Taxa de juros mensal (%): ", minimo=0.0)
    parcela_maxima = ler_float("Valor da parcela máxima (R$): ", minimo=0.0, estritamente_maior=True)
    limite_meses = ler_int("Limite máximo de meses: ", minimo=1)

    taxa = taxa_perc / 100.0
    mes = 0
    total_pago = 0.0
    total_juros = 0.0
    resultado = "Limite de meses atingido sem quitar a dívida"

    while mes < limite_meses and saldo > 1e-9:
        mes += 1
        juros_mes = saldo * taxa
        saldo_com_juros = saldo + juros_mes

        # Verifica se a parcela máxima consegue ao menos cobrir os juros gerados no mês
        if parcela_maxima <= juros_mes and saldo_com_juros > parcela_maxima:
            print(
                f"Mês {mes:2d}: Juros = R$ {juros_mes:,.2f} | Parcela máxima (R$ {parcela_maxima:,.2f}) "
                f"não supera os juros do mês."
            )
            resultado = "Interrompida: parcela insuficiente para reduzir a dívida"
            break

        parcela_efetiva = min(parcela_maxima, saldo_com_juros)
        saldo_restante = saldo_com_juros - parcela_efetiva
        if saldo_restante < 1e-6:
            saldo_restante = 0.0

        total_juros += juros_mes
        total_pago += parcela_efetiva
        saldo = saldo_restante

        print(
            f"Mês {mes:2d}: Juros = R$ {juros_mes:,.2f} | Parcela = R$ {parcela_efetiva:,.2f} "
            f"| Saldo restante = R$ {saldo:,.2f}"
        )

        if saldo == 0.0:
            resultado = "Dívida quitada com sucesso"
            break

    print("\n=== RESUMO DA SIMULAÇÃO ===")
    print(f"Total de meses: {mes}")
    print(f"Total pago: R$ {total_pago:,.2f}")
    print(f"Total de juros: R$ {total_juros:,.2f}")
    print(f"Saldo restante: R$ {saldo:,.2f}")
    print(f"Resultado da simulação: {resultado}")


if __name__ == "__main__":
    simular_financiamento()
