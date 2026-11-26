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


def analisar_vendedores() -> None:
    print("=== ANÁLISE DE VENDAS DE VENDEDORES ===")
    qtd_vendedores = ler_int("Quantidade de vendedores: ", minimo=1)

    total_vendido_equipe = 0.0
    total_comissoes_equipe = 0.0
    maior_venda = -1.0
    menor_venda = -1.0
    maior_vendedor = ""
    menor_vendedor = ""

    for i in range(1, qtd_vendedores + 1):
        print(f"\n--- Vendedor {i} de {qtd_vendedores} ---")
        while True:
            nome = input("Nome do vendedor: ").strip()
            if nome:
                break
            print("Erro: informe um nome válido.")

        salario_base = ler_float("Salário-base (R$): ", minimo=0.0)
        valor_vendido = ler_float("Valor total vendido (R$): ", minimo=0.0)
        qtd_vendas = ler_int("Quantidade de vendas: ", minimo=0)

        if valor_vendido <= 10000.0:
            taxa_comissao = 0.03
        elif valor_vendido <= 30000.0:
            taxa_comissao = 0.05
        else:
            taxa_comissao = 0.08

        comissao = valor_vendido * taxa_comissao
        bonus = 500.0 if qtd_vendas > 20 else 0.0
        remuneracao_final = salario_base + comissao + bonus
        media_por_venda = (valor_vendido / qtd_vendas) if qtd_vendas > 0 else 0.0

        total_vendido_equipe += valor_vendido
        total_comissoes_equipe += comissao

        if i == 1 or valor_vendido > maior_venda:
            maior_venda = valor_vendido
            maior_vendedor = nome

        if i == 1 or valor_vendido < menor_venda:
            menor_venda = valor_vendido
            menor_vendedor = nome

        print(f"Comissão ({taxa_comissao * 100:.0f}%): R$ {comissao:,.2f}")
        print(f"Bônus: R$ {bonus:,.2f}")
        print(f"Remuneração final: R$ {remuneracao_final:,.2f}")
        if qtd_vendas > 0:
            print(f"Média de valor por venda: R$ {media_por_venda:,.2f}")
        else:
            print("Média de valor por venda: N/A (0 vendas)")

    media_vendas_equipe = total_vendido_equipe / qtd_vendedores

    print("\n=== RESUMO DA EQUIPE ===")
    print(f"Total vendido pela equipe: R$ {total_vendido_equipe:,.2f}")
    print(f"Total pago em comissões: R$ {total_comissoes_equipe:,.2f}")
    print(f"Maior vendedor: {maior_vendedor} (R$ {maior_venda:,.2f})")
    print(f"Menor vendedor: {menor_vendedor} (R$ {menor_venda:,.2f})")
    print(f"Média de vendas da equipe: R$ {media_vendas_equipe:,.2f}")


if __name__ == "__main__":
    analisar_vendedores()
