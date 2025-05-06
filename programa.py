import funcoes as f

cartela = {'regra_simples': {i: -1 for i in range(1, 7)},'regra_avancada': {k: -1 for k in ['sem_combinacao', 'quadra', 'full_house','sequencia_baixa', 'sequencia_alta', 'cinco_iguais']}}
f.imprime_cartela(cartela)
rodadas = 0
