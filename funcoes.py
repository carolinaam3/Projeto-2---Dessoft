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
