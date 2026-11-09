class Veiculo:
    def __init__(self, marca, modelo, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
        self.disponivel = True

    def exibir_dados(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Quilometragem:", self.quilometragem)
        print("Disponível:", self.disponivel)
        print("--------------------------")

    def atualizar_quilometragem(self, nova_quilometragem):
        if nova_quilometragem > self.quilometragem:
            self.quilometragem = nova_quilometragem
            print("Quilometragem atualizada com sucesso!")
        else:
            print("Erro: a nova quilometragem não pode ser menor ou igual à atual.")

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print("Veículo alugado com sucesso!")
        else:
            print("Veículo indisponível para aluguel.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print("Veículo devolvido com sucesso!")
        else:
            print("O veículo já está disponível.")

    def pode_ser_alugado(self):
        return self.disponivel
