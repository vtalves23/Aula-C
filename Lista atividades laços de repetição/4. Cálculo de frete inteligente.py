def ler_float(mensagem: str, minimo: float = 0.0, estritamente_maior: bool = False) -> float:
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if estritamente_maior and valor <= minimo:
                print(f"Erro: informe um valor maior que {minimo}.")
                continue
            if not estritamente_maior and valor < minimo:
                print(f"Erro: informe um valor maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: digite um número válido.")


def ler_tipo_entrega() -> str:
    opcoes = {
        "1": "normal",
        "normal": "normal",
        "2": "expressa",
        "expressa": "expressa",
        "3": "urgente",
        "urgente": "urgente",
    }
    while True:
        escolha = input("Tipo de entrega (normal, expressa ou urgente): ").strip().lower()
        if escolha in opcoes:
            return opcoes[escolha]
        print("Erro: escolha entre 'normal', 'expressa' ou 'urgente'.")


def ler_assinante() -> bool:
    while True:
        resp = input("O cliente é assinante? (s/n): ").strip().lower()
        if resp in ("s", "sim", "y", "yes", "1", "true"):
            return True
        if resp in ("n", "nao", "não", "no", "0", "false"):
            return False
        print("Erro: responda com 's' (sim) ou 'n' (não).")


def calcular_frete() -> None:
    print("=== CÁLCULO DE FRETE INTELIGENTE ===")
    peso = ler_float("Peso da encomenda (kg): ", minimo=0.0, estritamente_maior=True)
    distancia = ler_float("Distância (km): ", minimo=0.0)
    tipo_entrega = ler_tipo_entrega()
    assinante = ler_assinante()
    valor_compra = ler_float("Valor da compra (R$): ", minimo=0.0)

    taxa_peso = peso * 2.50
    taxa_distancia = distancia * 0.30
    subtotal_base = taxa_peso + taxa_distancia

    # Adicionais
    if tipo_entrega == "expressa":
        perc_entrega = 0.30
    elif tipo_entrega == "urgente":
        perc_entrega = 0.60
    else:
        perc_entrega = 0.0

    adicional_entrega = subtotal_base * perc_entrega
    adicional_peso_excedente = 80.0 if peso > 30.0 else 0.0
    adicional_distancia_excedente = 100.0 if distancia > 500.0 else 0.0
    total_adicionais = adicional_entrega + adicional_peso_excedente + adicional_distancia_excedente

    valor_antes_desconto = subtotal_base + total_adicionais

    # Descontos (máximo de 20%)
    desconto_assinante = 0.15 if assinante else 0.0
    desconto_compra = 0.10 if valor_compra > 1000.0 else 0.0
    percentual_desconto_bruto = desconto_assinante + desconto_compra
    percentual_desconto_aplicado = min(0.20, percentual_desconto_bruto)
    valor_desconto = valor_antes_desconto * percentual_desconto_aplicado

    frete_calculado = valor_antes_desconto - valor_desconto

    # Regra de frete gratuito
    frete_gratis = (
        assinante
        and valor_compra >= 2000.0
        and tipo_entrega == "normal"
        and peso <= 10.0
    )

    frete_final = 0.0 if frete_gratis else frete_calculado

    print("\n--- DETALHAMENTO DO FRETE ---")
    print(f"Taxa por peso ({peso:.2f} kg x R$ 2,50): R$ {taxa_peso:,.2f}")
    print(f"Taxa por distância ({distancia:.2f} km x R$ 0,30): R$ {taxa_distancia:,.2f}")
    print(f"Subtotal base: R$ {subtotal_base:,.2f}")
    print(f"Adicional tipo de entrega ({tipo_entrega}, {perc_entrega * 100:.0f}%): R$ {adicional_entrega:,.2f}")
    print(f"Adicional peso > 30 kg: R$ {adicional_peso_excedente:,.2f}")
    print(f"Adicional distância > 500 km: R$ {adicional_distancia_excedente:,.2f}")
    print(f"Total de adicionais: R$ {total_adicionais:,.2f}")
    print(f"Valor antes do desconto: R$ {valor_antes_desconto:,.2f}")
    print(
        f"Desconto aplicado ({percentual_desconto_aplicado * 100:.0f}%"
        f"{' - teto de 20% aplicado' if percentual_desconto_bruto > 0.20 else ''}): -R$ {valor_desconto:,.2f}"
    )
    print(f"Frete após desconto: R$ {frete_calculado:,.2f}")
    print(f"Elegível a frete gratuito: {'Sim' if frete_gratis else 'Não'}")
    print(f"VALOR FINAL DO FRETE: R$ {frete_final:,.2f}")


if __name__ == "__main__":
    calcular_frete()
