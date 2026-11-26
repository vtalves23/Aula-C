def controle_estoque() -> None:
    estoque: dict[str, int] = {
        "teclado": 15,
        "mouse": 20,
        "monitor": 8,
        "notebook": 5,
    }

    # 1. Adicione o produto "webcam" com quantidade 10
    estoque["webcam"] = 10

    # 2. Atualize a quantidade de "mouse" para 25
    estoque["mouse"] = 25

    # 3. Remova "monitor" utilizando pop()
    removido = estoque.pop("monitor")
    print(f"Produto removido: monitor (quantidade: {removido})\n")

    # 4. Percorra o dicionário com items() e mostre produto e quantidade
    for produto, quantidade in estoque.items():
        print(f"Produto: {produto} | Quantidade: {quantidade}")

    # 5. Calcule e exiba a quantidade total de itens disponíveis no estoque
    total_itens = sum(estoque.values())
    print(f"\nQuantidade total de itens disponíveis no estoque: {total_itens}")


if __name__ == "__main__":
    controle_estoque()
