NUMERO_SECRETO = 42


def escolher_nivel() -> int:
    while True:
        print("\nEscolha o nível de dificuldade:")
        print("1 - Fácil (10 tentativas)")
        print("2 - Médio (7 tentativas)")
        print("3 - Difícil (5 tentativas)")
        escolha = input("Nível: ").strip().lower()

        if escolha in ("1", "facil", "fácil"):
            return 10
        if escolha in ("2", "medio", "médio"):
            return 7
        if escolha in ("3", "dificil", "difícil"):
            return 5
        print("Nível inválido! Digite 1, 2 ou 3 (ou fácil, médio, difícil).")


def jogo_adivinhacao() -> None:
    print("=== JOGO DE ADIVINHAÇÃO (1 A 100) ===")
    max_tentativas = escolher_nivel()
    tentativas_restantes = max_tentativas
    tentativas_utilizadas = 0
    venceu = False

    while tentativas_restantes > 0:
        entrada = input(f"\nDigite um número entre 1 e 100 (restam {tentativas_restantes}): ").strip().replace(",", ".")
        try:
            palpite = int(entrada)
        except ValueError:
            print("Entrada inválida! Digite um número inteiro entre 1 e 100 (tentativa não consumida).")
            continue

        if palpite < 1 or palpite > 100:
            print("Valor fora do intervalo de 1 a 100! (Tentativa não consumida).")
            continue

        tentativas_utilizadas += 1
        tentativas_restantes -= 1

        if palpite == NUMERO_SECRETO:
            venceu = True
            print("Parabéns! Você acertou o número secreto!")
            break
        elif palpite > NUMERO_SECRETO:
            print("O número secreto é MENOR que o valor digitado.")
        else:
            print("O número secreto é MAIOR que o valor digitado.")

        print(f"Tentativas restantes: {tentativas_restantes}")

    pontuacao = tentativas_restantes * 100 if venceu else 0

    print("\n=== RESULTADO FINAL ===")
    print(f"Resultado: {'Vitória' if venceu else 'Derrota'}")
    print(f"Número secreto: {NUMERO_SECRETO}")
    print(f"Tentativas utilizadas: {tentativas_utilizadas}")
    print(f"Pontuação: {pontuacao}")


if __name__ == "__main__":
    jogo_adivinhacao()
