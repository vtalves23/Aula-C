def dicionario_aninhado_alunos() -> None:
    turma: dict[str, dict[str, str | float]] = {
        "2026001": {"nome": "Ana", "nota": 8.5},
        "2026002": {"nome": "Bruno", "nota": 6.0},
        "2026003": {"nome": "Carla", "nota": 9.2},
    }

    soma_notas = 0.0

    for _, dados in turma.items():
        nome = str(dados["nome"])
        nota = float(dados["nota"])
        situacao = "Aprovado" if nota >= 7.0 else "Reprovado"
        soma_notas += nota

        print(f"{nome} - Nota: {nota:.1f} - Situação: {situacao}")

    media_geral = soma_notas / len(turma)
    print(f"\nMédia geral da turma: {media_geral:.2f}")


if __name__ == "__main__":
    dicionario_aninhado_alunos()
