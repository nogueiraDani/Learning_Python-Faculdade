# Aula sobre bibliotecas, em especial numpy
import time
import numpy



# 1 - Exemplo de criação:

print('-' * 50)
print('Criando nd arrays com numpy')
print('-' * 50)
nd_array_de_zeros = numpy.zeros(100000)
print(f'Conteúdo da lista: {nd_array_de_zeros}, o tamanho: {len(nd_array_de_zeros)}')

nd_array_de_uns = numpy.ones(100000)
print(f'Conteúdo da lista: {nd_array_de_uns}, o tamanho: {len(nd_array_de_uns)}')

nd_array_definido = numpy.linspace(10, 50, 15)
print(f'Conteúdo da lista: {nd_array_definido}, o tamanho: {len(nd_array_definido)}')

# 2 - Comparando desempenho
print('-' * 50)
print('Comparando desempenho')
print('-' * 50)
start_time = time.time()
lista = [0] * 1000000000
end_time = time.time()
elapsed_time = end_time - start_time
print(f'A criacao da lista de 1 bilhão de elementos levou: {elapsed_time} segundos')

start_time = time.time()
nd_array = numpy.zeros(1000000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(f'A criacao da lista de 1 bilhão de elementos levou: {elapsed_time} segundos')
print('-' * 50)

# 3 - Criando vetores, matrizes e tensores
rng = numpy.random.default_rng() #metodo random do numpy
# vetor
vetor = rng.random(4)
print(f'Array de 1 dimensao (vetor) com random: \n{vetor}\n')
# matriz
matriz = rng.random([4, 4])
print(f'Array de 2 dimensões (matriz) com random: \n{matriz}\n')
# tensor
tensor = rng.random([4, 4, 4])
print(f'Array de 3 dimensões (tensor) com random: \n{tensor}\n')

# 4 - Ordenar vetores
m_coluna = numpy.sort(matriz, axis=0)
m_linha = numpy.sort(matriz, axis=1)
m_col_lin = numpy.sort(m_linha, axis=0)
print('-' * 50)
print(f'Ordenação dentro coluna:\n{m_coluna}')
print(f'Ordenação dentro linha:\n{m_linha}')
print(f'Ordenação dentro coluna e linha:\n{m_col_lin}')

# 5 - Agora vamos preparar alguns ndarrays para serem representados por gráficos:
vetor_a = numpy.linspace(10, 1000, 100)
vetor_b = numpy.linspace(10, 3000, 100)
vetor_c = numpy.linspace(10, 8000, 100)

print(vetor_a)
print(vetor_b)
print(vetor_c)

# Numpy já tem métodos bem diretos de como salvar um arquivo no formato .txt
numpy.savetxt('vetor_a.txt', vetor_a, fmt='%f', delimiter=';')
numpy.savetxt('vetor_b.txt', vetor_b, fmt='%f', delimiter=';')
numpy.savetxt('vetor_c.txt', vetor_c, fmt='%f', delimiter=';')

# 6 - Agora podemos utilizar uma das várias bibliotecas para plotar gráficos, eu escolhi a plotly
import plotly.express

array_a = numpy.loadtxt('vetor_a.txt', dtype=numpy.float64, delimiter=';')
array_b = numpy.loadtxt('vetor_b.txt', dtype=numpy.float64, delimiter=';')
array_c = numpy.loadtxt('vetor_c.txt', dtype=numpy.float64, delimiter=';')
print(array_a)

array_abc = numpy.vstack([array_a, array_b, array_c])
print(array_abc)
array_abc = array_abc.transpose()
print(array_abc)
fig = plotly.express.line(array_abc)
fig.show()