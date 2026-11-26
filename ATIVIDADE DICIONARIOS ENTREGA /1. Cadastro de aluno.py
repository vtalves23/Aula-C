def cadastro_aluno() -> None:
    aluno: dict[str, str | int | float] = {
        "nome": "Carlos",
        "idade": 21,
        "curso": "Sistemas de Informação",
        "nota": 7.0,
    }

    # 1. Exiba o nome e o curso do aluno
    print(f"Nome: {aluno['nome']} | Curso: {aluno['curso']}")

    # 2. Altere a nota para 8.5
    aluno["nota"] = 8.5

    # 3. Adicione a chave "situacao" com o valor "Aprovado"
    aluno["situacao"] = "Aprovado"

    # 4. Exiba o dicionário completo ao final
    print("Dicionário completo:", aluno)


if __name__ == "__main__":
    cadastro_aluno()
