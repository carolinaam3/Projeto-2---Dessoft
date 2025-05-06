import funcoes as f

cartela = {'regra_simples': {i: -1 for i in range(1, 7)},'regra_avancada': {k: -1 for k in ['sem_combinacao', 'quadra', 'full_house','sequencia_baixa', 'sequencia_alta', 'cinco_iguais']}}
f.imprime_cartela(cartela)

while -1 in cartela['regra_simples'].values() or -1 in cartela['regra_avancada'].values():
    dados_rolados = f.rolar_dados(5)
    dados_guardados = []
    reroladas = 0
    rodada_em_andamento = True

    while rodada_em_andamento:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()
        

        if opcao == '1':
            print(f"Digite o índice do dado a ser guardado (0 a 4):")
            resposta = int(input())
            dados_rolados, dados_guardados = f.guardar_dado(dados_rolados, dados_guardados, resposta)

        elif opcao == '2':
            print(f"Digite o índice do dado a ser removido (0 a 4):")
            resposta = int(input())
            dados_rolados, dados_guardados = f.remover_dado(dados_rolados, dados_guardados, resposta)

        elif opcao == '3':
            if reroladas < 2:
                dados_rolados = f.rolar_dados(len(dados_rolados))
                reroladas += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == '4':
            f.imprime_cartela(cartela)
        elif opcao == '0':
            while True:
                print("Digite a combinação desejada:")
                combo = input()
                if combo.isdigit():
                    key = int(combo)
                    if key in cartela['regra_simples']:
                        if cartela['regra_simples'][key] == -1:
                            f.faz_jogada(dados_rolados + dados_guardados, key, cartela)
                            break
                        else:
                            print("Essa combinação já foi utilizada. Escolha outra.")
                    else:
                        print("Combinação inválida. Tente novamente.")
                elif combo in cartela['regra_avancada']:
                    if cartela['regra_avancada'][combo] == -1:
                        f.faz_jogada(dados_rolados + dados_guardados, combo, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada. Escolha outra.")
                else:
                    print("Combinação inválida. Tente novamente.")
            break  

        else:
            print("Opção inválida. Tente novamente.")


total_simples = sum(cartela['regra_simples'].values())
total_avancada = sum(cartela['regra_avancada'].values())
total = total_simples + total_avancada + (35 if total_simples >= 63 else 0)

f.imprime_cartela(cartela)
print(f"Pontuação total: {total}")