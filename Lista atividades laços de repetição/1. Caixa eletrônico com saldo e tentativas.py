SENHA_CORRETA = "1234"
MAX_TENTATIVAS = 3


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


def caixa_eletronico() -> None:
    print("=== CAIXA ELETRÔNICO ===")
    autenticado = False

    for tentativa in range(1, MAX_TENTATIVAS + 1):
        senha = input(f"Digite a senha (tentativa {tentativa}/{MAX_TENTATIVAS}): ").strip()
        if senha == SENHA_CORRETA:
            autenticado = True
            print("Autenticação realizada com sucesso!")
            break
        restantes = MAX_TENTATIVAS - tentativa
        if restantes > 0:
            print(f"Senha incorreta. Tentativas restantes: {restantes}")
        else:
            print("Senha incorreta. Cartão bloqueado por excesso de tentativas.")

    if not autenticado:
        return

    saldo = ler_float("Informe o saldo inicial da conta (R$): ", minimo=0.0)
    saldo_inicial = saldo

    qtd_depositos = 0
    qtd_saques = 0
    total_depositado = 0.0
    total_sacado = 0.0

    while True:
        print("\n--- MENU ---")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Exibir quantidade de operações")
        print("5 - Encerrar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print(f"Saldo atual: R$ {saldo:,.2f}")

        elif opcao == "2":
            valor_deposito = ler_float("Valor do depósito (R$): ")
            if valor_deposito <= 0:
                print("Operação negada: o valor do depósito deve ser maior que zero.")
            else:
                saldo += valor_deposito
                qtd_depositos += 1
                total_depositado += valor_deposito
                print(f"Depósito realizado! Novo saldo: R$ {saldo:,.2f}")

        elif opcao == "3":
            valor_saque = ler_float("Valor do saque (R$): ")
            if valor_saque <= 0:
                print("Operação negada: o valor do saque deve ser maior que zero.")
            elif valor_saque > saldo:
                print(f"Operação negada: saldo insuficiente (disponível: R$ {saldo:,.2f}).")
            else:
                saldo -= valor_saque
                qtd_saques += 1
                total_sacado += valor_saque
                print(f"Saque realizado! Novo saldo: R$ {saldo:,.2f}")

        elif opcao == "4":
            total_operacoes = qtd_depositos + qtd_saques
            print(f"Depósitos realizados: {qtd_depositos}")
            print(f"Saques realizados: {qtd_saques}")
            print(f"Total de operações (depósitos + saques): {total_operacoes}")

        elif opcao == "5":
            print("\n=== RELATÓRIO FINAL DO CAIXA ELETRÔNICO ===")
            print(f"Saldo inicial: R$ {saldo_inicial:,.2f}")
            print(f"Quantidade de depósitos: {qtd_depositos}")
            print(f"Quantidade de saques: {qtd_saques}")
            print(f"Quantidade total de operações: {qtd_depositos + qtd_saques}")
            print(f"Total depositado: R$ {total_depositado:,.2f}")
            print(f"Total sacado: R$ {total_sacado:,.2f}")
            print(f"Saldo final: R$ {saldo:,.2f}")
            print("Sessão encerrada.")
            break

        else:
            print("Opção inexistente! Escolha entre 1 e 5.")


if __name__ == "__main__":
    caixa_eletronico()
