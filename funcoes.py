import random
def rolar_dados(n):
    lista = []
    for i in range(n):
        x = random.randint(1,6)
        lista.append(x)
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, indice):
    dados_no_estoque.append(dados_rolados[indice])
    del dados_rolados[indice]
    
    lista= [dados_rolados,dados_no_estoque]
    
    return lista 

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    del dados_no_estoque[dado_para_remover]
    return [dados_rolados,dados_no_estoque]

def calcula_pontos_regra_simples(lista):
    dicionário = {}
    for i in range(6):
        dicionário[i+1] = 0
    for i in lista:
         dicionário[i] += i
    return dicionário  

def calcula_pontos_soma (lista):
    soma = 0
    for i in lista:
        soma+=i
    return soma 

def calcula_pontos_sequencia_baixa (lista):
    lista = list(set(lista))
    ordenado = sorted(lista, reverse=False)
    for i in range(len(lista)-3):
        if lista[i] == lista[i+1]-1 == lista[i+2]-2 == lista[i+3]-3:
            return 15
    return 0

def calcula_pontos_sequencia_alta(lista):
    lista = list(set(lista))
    ordenado = sorted(lista, reverse=False)
    for i in range(len(lista)-4):
        if lista[i] == lista[i+1]-1 == lista[i+2]-2 == lista[i+3]-3 == lista[i+4]-4:
            return 30
    return 0

def calcula_pontos_full_house(lista):
    quantidade_de_numeros = list(set(lista))
    ordenado = sorted(lista, reverse=False)
    if len(quantidade_de_numeros) != 2:
        return 0
    elif ordenado[1] != ordenado[2] or ordenado[2] != ordenado[3]:
        soma = 0
        for i in lista:
            soma += i
        return soma
    else:
        return 0

def calcula_pontos_quadra(lista):
    lista = sorted(lista, reverse=False)
    for i in range(len(lista)-3):
        if lista[i] == lista[i+1] == lista[i+2] == lista[i+3]:
            soma = 0
            for i in lista:
                soma += i
            return soma
    return 0


def calcula_pontos_quina(lista):
    lista = sorted(lista, reverse=False)
    for i in range(len(lista)-4):
        if lista[i] == lista[i+1] == lista[i+2] == lista[i+3] == lista[i+4]:
            return 50
    return 0

def calcula_pontos_regra_avancada(lista):
    dicionario = {}
    dicionario['cinco_iguais'] = calcula_pontos_quina(lista)
    dicionario['full_house'] = calcula_pontos_full_house(lista)
    dicionario['quadra'] = calcula_pontos_quadra(lista)
    dicionario['sem_combinacao'] = calcula_pontos_soma(lista)
    dicionario['sequencia_alta'] =  calcula_pontos_sequencia_alta(lista)
    dicionario['sequencia_baixa'] =  calcula_pontos_sequencia_baixa(lista)
    return dicionario

def faz_jogada (lista,categoria,dic):
    regra_sim = ['1','2','3','4','5','6']
    if categoria in regra_sim:
        dic['regra_simples'][int(categoria)] = calcula_pontos_regra_simples(lista)[int(categoria)]
    elif categoria in dic['regra_avancada']:
        dic['regra_avancada'][categoria] = calcula_pontos_regra_avancada(lista)[categoria]
    return dic

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)