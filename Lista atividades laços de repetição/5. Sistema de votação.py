def sistema_votacao() -> None:
    votos_a = 0
    votos_b = 0
    votos_c = 0
    votos_branco = 0
    votos_nulo = 0

    print("=== SISTEMA DE VOTAÇÃO ===")

    while True:
        print("\nOpções de voto:")
        print("1 - Candidato A")
        print("2 - Candidato B")
        print("3 - Candidato C")
        print("4 - Voto em branco")
        print("5 - Voto nulo")
        print("0 - Encerrar votação")

        opcao = input("Digite seu voto: ").strip()

        if opcao == "1":
            votos_a += 1
            print("Voto registrado para o Candidato A.")
        elif opcao == "2":
            votos_b += 1
            print("Voto registrado para o Candidato B.")
        elif opcao == "3":
            votos_c += 1
            print("Voto registrado para o Candidato C.")
        elif opcao == "4":
            votos_branco += 1
            print("Voto em branco registrado.")
        elif opcao == "5":
            votos_nulo += 1
            print("Voto nulo registrado.")
        elif opcao == "0":
            print("Encerrando votação...")
            break
        else:
            print("Opção inválida! Digite um número de 0 a 5.")

    total_votos = votos_a + votos_b + votos_c + votos_branco + votos_nulo
    votos_validos = votos_a + votos_b + votos_c
    votos_invalidos = votos_branco + votos_nulo

    print("\n=== RESULTADO DA VOTAÇÃO ===")
    print(f"Candidato A: {votos_a} voto(s)")
    print(f"Candidato B: {votos_b} voto(s)")
    print(f"Candidato C: {votos_c} voto(s)")
    print(f"Votos em branco: {votos_branco}")
    print(f"Votos nulos: {votos_nulo}")
    print(f"Total de votos: {total_votos}")

    if total_votos == 0:
        print("Nenhum voto foi registrado.")
        return

    perc_a = (votos_a / total_votos) * 100.0
    perc_b = (votos_b / total_votos) * 100.0
    perc_c = (votos_c / total_votos) * 100.0
    perc_validos = (votos_validos / total_votos) * 100.0
    perc_invalidos = (votos_invalidos / total_votos) * 100.0

    print(f"Percentual Candidato A (sobre o total): {perc_a:.2f}%")
    print(f"Percentual Candidato B (sobre o total): {perc_b:.2f}%")
    print(f"Percentual Candidato C (sobre o total): {perc_c:.2f}%")
    print(f"Percentual de votos válidos: {perc_validos:.2f}%")
    print(f"Percentual de votos inválidos (brancos + nulos): {perc_invalidos:.2f}%")

    if votos_validos == 0:
        print("Vencedor: Não há vencedor (nenhum voto válido registrado).")
        print("Empate: Não aplicável.")
        return

    maior_voto = votos_a
    if votos_b > maior_voto:
        maior_voto = votos_b
    if votos_c > maior_voto:
        maior_voto = votos_c

    empatados_a = votos_a == maior_voto
    empatados_b = votos_b == maior_voto
    empatados_c = votos_c == maior_voto
    qtd_empatados = (1 if empatados_a else 0) + (1 if empatados_b else 0) + (1 if empatados_c else 0)

    if qtd_empatados > 1:
        nomes_empatados = ""
        if empatados_a:
            nomes_empatados += "Candidato A"
        if empatados_b:
            nomes_empatados += (", " if nomes_empatados else "") + "Candidato B"
        if empatados_c:
            nomes_empatados += (", " if nomes_empatados else "") + "Candidato C"
        print(f"Empate: Sim — empataram com {maior_voto} voto(s): {nomes_empatados}.")
        print("Vencedor: Indefinido devido a empate.")
    else:
        if empatados_a:
            vencedor = "Candidato A"
        elif empatados_b:
            vencedor = "Candidato B"
        else:
            vencedor = "Candidato C"
        print(f"Empate: Não")
        print(f"Vencedor: {vencedor} ({maior_voto} voto(s))")


if __name__ == "__main__":
    sistema_votacao()
