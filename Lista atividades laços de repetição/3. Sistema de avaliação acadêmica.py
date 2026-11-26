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


def ler_int(mensagem: str, minimo: int = 0, estritamente_maior: bool = False) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if estritamente_maior and valor <= minimo:
                print(f"Erro: informe um inteiro maior que {minimo}.")
                continue
            if not estritamente_maior and valor < minimo:
                print(f"Erro: informe um inteiro maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def avaliar_aluno() -> None:
    print("=== SISTEMA DE AVALIAÇÃO ACADÊMICA ===")
    n1 = ler_float("Nota 1 (0 a 10): ", minimo=0.0, maximo=10.0)
    n2 = ler_float("Nota 2 (0 a 10): ", minimo=0.0, maximo=10.0)
    n3 = ler_float("Nota 3 (0 a 10): ", minimo=0.0, maximo=10.0)
    frequencia = ler_float("Percentual de frequência (0 a 100): ", minimo=0.0, maximo=100.0)
    total_atividades = ler_int("Quantidade total de atividades: ", minimo=0, estritamente_maior=True)

    while True:
        atividades_entregues = ler_int("Quantidade de atividades entregues: ", minimo=0)
        if atividades_entregues > total_atividades:
            print(f"Erro: atividades entregues não podem ultrapassar o total ({total_atividades}).")
        else:
            break

    media = (n1 + n2 + n3) / 3.0
    perc_atividades = (atividades_entregues / total_atividades) * 100.0

    # Classificação principal
    if frequencia < 75.0:
        classificacao = "Reprovado por frequência"
    elif media < 5.0:
        classificacao = "Reprovado por nota"
    elif media >= 9.0 and frequencia >= 90.0 and atividades_entregues == total_atividades:
        classificacao = "Aprovado com excelência"
    elif media >= 7.0 and frequencia >= 75.0 and perc_atividades >= 70.0:
        classificacao = "Aprovado"
    else:
        classificacao = "Recuperação"

    # Principal requisito que impediu uma classificação superior
    if classificacao == "Aprovado com excelência":
        impedimento = "Nenhum — o aluno alcançou a classificação máxima possível."
    elif classificacao == "Aprovado":
        # Classificação superior possível: Aprovado com excelência
        if media < 9.0:
            impedimento = f"Média inferior a 9,0 (média atual: {media:.2f}) para 'Aprovado com excelência'."
        elif frequencia < 90.0:
            impedimento = f"Frequência inferior a 90% (atual: {frequencia:.2f}%) para 'Aprovado com excelência'."
        else:
            impedimento = (
                f"Não entregou todas as atividades ({atividades_entregues}/{total_atividades}) "
                "para 'Aprovado com excelência'."
            )
    elif classificacao == "Recuperação":
        # Classificação superior possível: Aprovado
        if media < 7.0:
            impedimento = f"Média inferior a 7,0 (média atual: {media:.2f}) para 'Aprovado'."
        elif perc_atividades < 70.0:
            impedimento = (
                f"Percentual de atividades entregues ({perc_atividades:.2f}%) inferior a 70% para 'Aprovado'."
            )
        else:
            impedimento = "Requisitos de 'Aprovado' não atingidos."
    elif classificacao == "Reprovado por nota":
        # Acima de Reprovado por nota: Recuperação (média >= 5 e frequência >= 75%)
        impedimento = f"Média inferior a 5,0 (média atual: {media:.2f}) para 'Recuperação'."
    else:
        # Reprovado por frequência: frequência < 75% impede Recuperação, Aprovado e Excelência
        impedimento = f"Frequência inferior a 75% (atual: {frequencia:.2f}%), impedindo aprovação ou recuperação."

    print("\n--- BOLETIM E CLASSIFICAÇÃO ---")
    print(f"Média das notas: {media:.2f}")
    print(f"Frequência: {frequencia:.2f}%")
    print(f"Atividades entregues: {atividades_entregues}/{total_atividades} ({perc_atividades:.2f}%)")
    print(f"Classificação: {classificacao}")
    print(f"Principal requisito que impediu classificação superior: {impedimento}")


if __name__ == "__main__":
    avaliar_aluno()
