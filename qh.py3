from sys import stdin

def custo_da_rota(distancias, rota):
    custo = sum(distancias[rota[i]][rota[i+1]] for i in range(len(rota)-1))
    custo += distancias[rota[-1]][rota[0]]
    return custo

def gera_melhor_rota(n_cidades, distancias):
    rota_padrao = list(range(n_cidades))
    custo_padrao = custo_da_rota(distancias, rota_padrao)

    melhor_custo = custo_padrao
    rotas_com_menor_custo = 1

    for i in range(1, n_cidades-1):
        for j in range(i+1, n_cidades):
            nova_rota = rota_padrao.copy()
            nova_rota[i], nova_rota[j] = nova_rota[j], nova_rota[i]
            custo_nova_rota = custo_da_rota(distancias, nova_rota)
            if custo_nova_rota == melhor_custo:
                rotas_com_menor_custo += 1
            elif custo_nova_rota < melhor_custo:
                melhor_custo = custo_nova_rota
                rotas_com_menor_custo = 1

    return custo_padrao, rotas_com_menor_custo, melhor_custo


if __name__ == '__main__':
    try:
        while True:
            n_cidades = int(input())
            temp, vel = map(int, input().split())
            distancias = [list(map(int, input().split())) for _ in range(n_cidades)]
            custo_padrao, n_melhor, melhor_custo = gera_melhor_rota(n_cidades, distancias)
            print("Numero de cidades: {}".format(n_cidades))
            print("Custo da rota padrao: {}".format(custo_padrao))
            print("Custo da rota economica: {}".format(melhor_custo))
            print("Numeros de rotas com o menor custo: {}".format(n_melhor))
            dur_padrao = (custo_padrao/vel)*60
            dur_melhor = (melhor_custo/vel)*60
            n_padrao = temp*60/dur_padrao
            n_melhor = temp*60/dur_melhor
            print("Duracao de uma viagem (em minutos) percorrendo a rota padrao: {:.2f}".format(dur_padrao))
            print("Duracao de cada viagem (em minutos) percorrendo a rota economica: {:.2f}".format(dur_melhor))
            print("Numero de partidas das viagens durante o expediente (a rota padrao): {}".format(int(n_padrao)))
            print("Numero de partidas das viagens durante o expediente (a rota economica): {}".format(int(n_melhor)))
            print("Banco de horas (em minutos): {:.2f}".format(temp*60 % dur_melhor))
            print("Percentual de aumento de numero de rotas: {:.2f}%".format(((100*int(n_melhor))/int(n_padrao))-100))
    except:
        pass