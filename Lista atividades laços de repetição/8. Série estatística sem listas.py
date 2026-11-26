def ler_int(mensagem: str, minimo: int | None = None) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Erro: informe um inteiro maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def serie_estatistica() -> None:
    print("=== SÉRIE ESTATÍSTICA (SEM LISTAS) ===")
    qtd = ler_int("Quantidade de números: ", minimo=1)

    soma = 0
    positivos = 0
    negativos = 0
    zeros = 0
    pares = 0
    impares = 0
    maior = 0
    menor = 0

    for i in range(1, qtd + 1):
        num = ler_int(f"Digite o {i}º número inteiro: ")

        if i == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num

        soma += num

        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
        else:
            zeros += 1

        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    media = soma / qtd
    perc_positivos = (positivos / qtd) * 100.0
    perc_pares = (pares / qtd) * 100.0

    print("\n=== ESTATÍSTICAS DA SÉRIE ===")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Quantidade de positivos: {positivos}")
    print(f"Quantidade de negativos: {negativos}")
    print(f"Quantidade de zeros: {zeros}")
    print(f"Quantidade de pares: {pares}")
    print(f"Quantidade de ímpares: {impares}")
    print(f"Percentual de números positivos: {perc_positivos:.2f}%")
    print(f"Percentual de números pares: {perc_pares:.2f}%")


if __name__ == "__main__":
    serie_estatistica()
