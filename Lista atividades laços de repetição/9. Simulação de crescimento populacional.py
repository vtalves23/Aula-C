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


def simular_crescimento_populacional() -> None:
    print("=== SIMULAÇÃO DE CRESCIMENTO POPULACIONAL ===")
    pop_a = ler_float("População inicial da cidade A: ", minimo=0.0, estritamente_maior=True)
    taxa_a = ler_float("Taxa anual de crescimento da cidade A (%): ") / 100.0
    pop_b = ler_float("População inicial da cidade B: ", minimo=0.0, estritamente_maior=True)
    taxa_b = ler_float("Taxa anual de crescimento da cidade B (%): ") / 100.0
    max_anos = ler_int("Quantidade máxima de anos: ", minimo=1)

    menor_era_a = pop_a < pop_b
    menor_era_b = pop_b < pop_a

    anos_necessarios = 0
    houve_ultrapassagem = False

    print(f"\nAno 0 -> Cidade A: {pop_a:,.0f} | Cidade B: {pop_b:,.0f}")

    for ano in range(1, max_anos + 1):
        pop_a = pop_a * (1.0 + taxa_a)
        pop_b = pop_b * (1.0 + taxa_b)
        anos_necessarios = ano

        print(f"Ano {ano:2d} -> Cidade A: {pop_a:,.2f} | Cidade B: {pop_b:,.2f}")

        if (menor_era_a and pop_a > pop_b) or (menor_era_b and pop_b > pop_a):
            houve_ultrapassagem = True
            print("Ultrapassagem detectada! Encerrando simulação.")
            break

    diferenca_final = abs(pop_a - pop_b)

    print("\n=== RESULTADO DA SIMULAÇÃO POPULACIONAL ===")
    print(f"Quantidade de anos necessários: {anos_necessarios}")
    print(f"População final da cidade A: {pop_a:,.2f}")
    print(f"População final da cidade B: {pop_b:,.2f}")
    print(f"Diferença final entre as populações: {diferenca_final:,.2f}")
    print(f"Houve ultrapassagem: {'Sim' if houve_ultrapassagem else 'Não'}")


if __name__ == "__main__":
    simular_crescimento_populacional()
