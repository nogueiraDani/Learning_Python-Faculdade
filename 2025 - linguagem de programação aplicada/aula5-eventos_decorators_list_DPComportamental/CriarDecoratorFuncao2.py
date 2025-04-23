# ---------------------------------------------------------------------------------------------------------------------
import time


# Definindo o decorator para medir o tempo de execução
def medir_tempo(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs) # *args = argumentos generitcos | *kwargs = argumentos complexos
        fim = time.time()
        print(f"A função '{funcao.__name__}' demorou {fim - inicio:.6f} segundos para ser executada.")
        return resultado

    return wrapper


# Aplicando o decorator usando o símbolo @
@medir_tempo
def exemplo_funcao(tempo_espera):
    time.sleep(tempo_espera)
    print("A função foi executada.")


@medir_tempo
def exemplo_funcao2(tempo_espera):
    time.sleep(tempo_espera)
    print("A função foi executada.")


# Chamando a função decorada
exemplo_funcao(2)
exemplo_funcao2(4)
# ---------------------------------------------------------------------------------------------------------------------