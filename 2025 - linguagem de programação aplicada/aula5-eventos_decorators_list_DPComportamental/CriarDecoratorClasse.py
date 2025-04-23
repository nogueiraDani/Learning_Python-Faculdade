# ---------------------------------------------------------------------------------------------------------------------

# Definindo classe Carro
class Carro:
    def __init__(self, classe_decorada):
        self.classe_decorada = classe_decorada

    def __call__(self, *args, **kwargs):
        # instancia a classe original
        instancia_classe = self.classe_decorada(*args, **kwargs)

        # adiciona atributo extra
        instancia_classe.num_rodas = 4
        return instancia_classe


# Aplicando o decorator para indicar um variacao de heranca
@Carro
class Automovel:
    def __init__(self, nome):
        self.nome = nome


# Criando uma instancia de classe decorada
new_auto = Automovel('Gol')

# Chamando o metodo da classe e exibindo atributo extra
print(new_auto.nome)
print(new_auto.num_rodas)

# ---------------------------------------------------------------------------------------------------------------------
