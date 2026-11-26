def ler_float(mensagem: str, minimo: float = 0.0, maximo: float | None = None) -> float:
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < minimo or (maximo is not None and valor > maximo):
                if maximo is not None:
                    print(f"Erro: informe um valor entre {minimo} e {maximo}.")
                else:
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


def relatorio_turma() -> None:
    print("=== RELATÓRIO DE DESEMPENHO DA TURMA ===")
    qtd_alunos = ler_int("Quantidade de alunos: ", minimo=1)

    soma_medias = 0.0
    maior_media = -1.0
    menor_media = 11.0
    melhor_aluno = ""
    pior_aluno = ""

    qtd_aprovados = 0
    qtd_recuperacao = 0
    qtd_reprovados = 0

    for i in range(1, qtd_alunos + 1):
        print(f"\n--- Aluno {i} de {qtd_alunos} ---")
        while True:
            nome = input("Nome do aluno: ").strip()
            if nome:
                break
            print("Erro: o nome não pode ficar em branco.")

        n1 = ler_float("Nota 1 (0 a 10): ", minimo=0.0, maximo=10.0)
        n2 = ler_float("Nota 2 (0 a 10): ", minimo=0.0, maximo=10.0)
        n3 = ler_float("Nota 3 (0 a 10): ", minimo=0.0, maximo=10.0)
        frequencia = ler_float("Frequência (0 a 100%): ", minimo=0.0, maximo=100.0)

        media = (n1 + n2 + n3) / 3.0

        # Regra padrão: frequência >= 75% para aprovação/recuperação; média >= 7 aprovado, 5..6.99 recuperação
        if frequencia < 75.0:
            situacao = "Reprovado (frequência abaixo de 75%)"
            qtd_reprovados += 1
        elif media >= 7.0:
            situacao = "Aprovado"
            qtd_aprovados += 1
        elif media >= 5.0:
            situacao = "Recuperação"
            qtd_recuperacao += 1
        else:
            situacao = "Reprovado (média abaixo de 5,0)"
            qtd_reprovados += 1

        soma_medias += media

        if i == 1 or media > maior_media:
            maior_media = media
            melhor_aluno = nome

        if i == 1 or media < menor_media:
            menor_media = media
            pior_aluno = nome

        print(f"-> {nome}: Média = {media:.2f} | Frequência = {frequencia:.1f}% | Situação = {situacao}")

    media_geral = soma_medias / qtd_alunos
    perc_aprovacao = (qtd_aprovados / qtd_alunos) * 100.0

    print("\n=== RESUMO GERAL DA TURMA ===")
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Maior média: {maior_media:.2f} (Aluno: {melhor_aluno})")
    print(f"Menor média: {menor_media:.2f} (Aluno: {pior_aluno})")
    print(f"Quantidade de aprovados: {qtd_aprovados}")
    print(f"Quantidade em recuperação: {qtd_recuperacao}")
    print(f"Quantidade reprovada: {qtd_reprovados}")
    print(f"Percentual de aprovação: {perc_aprovacao:.2f}%")


if __name__ == "__main__":
    relatorio_turma()
