from code.dp_builder.Casa import Casa

class CasaBuilder:
    def __init__(self):
        self.casa = Casa()

    def set_num_quartos(self, num_quartos):
        self.casa.num_quartos = num_quartos
        return self

    def set_num_banheiros(self, num_banheiros):
        self.casa.num_banheiros = num_banheiros
        return self

    def adicionar_garagem(self):
        self.casa.tem_garagem = True
        return self

    def adicionar_jardim(self):
        self.casa.tem_jardim = True
        return self

    def obter_casa(self):
        return self.casa