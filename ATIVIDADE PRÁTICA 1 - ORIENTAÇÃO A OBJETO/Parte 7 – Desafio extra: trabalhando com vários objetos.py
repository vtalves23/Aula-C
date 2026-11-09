frota = [veiculo1, veiculo2, veiculo3]

for veiculo in frota:
    veiculo.exibir_dados()

print("Veículos disponíveis:")

for veiculo in frota:
    if veiculo.disponivel:
        print(veiculo.modelo)
