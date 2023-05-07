from sys import stdin

def add(a, b):
    return a+b

def reduce(func, li):
    a = 0
    for x in li:
        a =  func(a, x)
    return a

n, m = map(int,input().split())
prices = list(map(int,input().split()))

players = [tuple(map(int,x.split())) for x in  stdin]

out = []

for player in players:
    moedas, nivelAtual = player

    while nivelAtual < m and moedas >= prices[nivelAtual]:
        moedas -= prices[nivelAtual]
        nivelAtual += 1

    atk = reduce(add, range(nivelAtual+1))
    out.append(str(atk))

print(' '.join(out))
