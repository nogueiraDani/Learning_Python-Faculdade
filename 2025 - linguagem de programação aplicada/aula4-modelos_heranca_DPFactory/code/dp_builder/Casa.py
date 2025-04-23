class Casa:
    def __init__(self):
        self.num_quartos = None
        self.num_banheiros = None
        self.tem_garagem = False
        self.tem_jardim = False

    def __str__(self):
        caracteristicas = []
        if self.num_quartos:
            caracteristicas.append(f"Número de quartos: {self.num_quartos}")
        if self.num_banheiros:
            caracteristicas.append(f"Número de banheiros: {self.num_banheiros}")
        if self.tem_garagem:
            caracteristicas.append("Possui garagem")
        if self.tem_jardim:
            caracteristicas.append("Possui jardim")

        return ', '.join(caracteristicas)