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


def controle_estoque() -> None:
    estoque_inicial = 100.0
    estoque = estoque_inicial
    estoque_minimo = 20.0

    qtd_entradas = 0
    qtd_saidas = 0
    total_entradas = 0.0
    total_saidas = 0.0
    total_movimentado = 0.0

    print("=== CONTROLE DE ESTOQUE ===")
    print(f"Estoque inicial: {estoque:.2f} | Estoque mínimo padrão: {estoque_minimo:.2f}")

    while True:
        print("\n--- MENU DE ESTOQUE ---")
        print("1 - Entrada de mercadoria")
        print("2 - Saída de mercadoria")
        print("3 - Consultar estoque")
        print("4 - Definir estoque mínimo")
        print("5 - Encerrar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            qtd = ler_float("Quantidade de entrada: ")
            if qtd <= 0:
                print("Erro: a entrada deve ser maior que zero.")
            else:
                estoque += qtd
                qtd_entradas += 1
                total_entradas += qtd
                total_movimentado += qtd
                print(f"Entrada registrada! Estoque atual: {estoque:.2f}")
                if estoque < estoque_minimo:
                    print(f"ALERTA: estoque ({estoque:.2f}) abaixo do mínimo ({estoque_minimo:.2f})!")

        elif opcao == "2":
            qtd = ler_float("Quantidade de saída: ")
            if qtd <= 0:
                print("Erro: a saída deve ser maior que zero.")
            elif qtd > estoque:
                print(f"Erro: saída ({qtd:.2f}) ultrapassa o estoque disponível ({estoque:.2f}).")
            else:
                estoque -= qtd
                qtd_saidas += 1
                total_saidas += qtd
                total_movimentado += qtd
                print(f"Saída registrada! Estoque atual: {estoque:.2f}")
                if estoque < estoque_minimo:
                    print(f"ALERTA: estoque ({estoque:.2f}) abaixo do mínimo ({estoque_minimo:.2f})!")

        elif opcao == "3":
            situacao = "ABAIXO DO MÍNIMO" if estoque < estoque_minimo else "NORMAL"
            print(f"Estoque atual: {estoque:.2f} | Estoque mínimo: {estoque_minimo:.2f} | Situação: {situacao}")
            if estoque < estoque_minimo:
                print(f"ALERTA: estoque abaixo do mínimo definido ({estoque_minimo:.2f})!")

        elif opcao == "4":
            novo_minimo = ler_float("Novo estoque mínimo: ", minimo=0.0)
            estoque_minimo = novo_minimo
            print(f"Estoque mínimo atualizado para {estoque_minimo:.2f}.")
            if estoque < estoque_minimo:
                print(f"ALERTA: estoque atual ({estoque:.2f}) já está abaixo do novo mínimo!")

        elif opcao == "5":
            quantidade_operacoes = qtd_entradas + qtd_saidas
            if estoque <= 0:
                situacao_final = "Zerado"
            elif estoque < estoque_minimo:
                situacao_final = "Abaixo do mínimo"
            else:
                situacao_final = "Regular"

            print("\n=== RELATÓRIO FINAL DE ESTOQUE ===")
            print(f"Estoque inicial: {estoque_inicial:.2f}")
            print(f"Total de entradas: {total_entradas:.2f} ({qtd_entradas} operação(ões))")
            print(f"Total de saídas: {total_saidas:.2f} ({qtd_saidas} operação(ões))")
            print(f"Total movimentado: {total_movimentado:.2f}")
            print(f"Estoque final: {estoque:.2f}")
            print(f"Quantidade de operações: {quantidade_operacoes}")
            print(f"Situação do estoque: {situacao_final}")
            break

        else:
            print("Opção inválida! Escolha entre 1 e 5.")


if __name__ == "__main__":
    controle_estoque()
