def consulta_segura() -> None:
    produto: dict[str, str | float | int] = {
        "nome": "Notebook",
        "preco": 4500.00,
        "estoque": 12,
    }

    chave = input("Digite a informação desejada: ").strip()
    valor = produto.get(chave, "Informação não encontrada.")
    print(valor)


if __name__ == "__main__":
    consulta_segura()
