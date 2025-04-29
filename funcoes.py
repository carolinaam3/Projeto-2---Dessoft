import random
def rolar_dados(n):
    lista = []
    for i in range(n):
        x = random.randint(1,6)
        lista.append(x)
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, indice):
    dados_no_estoque.append(dados_rolados[indice])
    dados_rolados2 = dados_rolados.remove(dados_rolados[indice])
    lista= [dados_rolados2,dados_no_estoque]
    
    return lista 
