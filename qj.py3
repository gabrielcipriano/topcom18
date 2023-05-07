from sys import stdin
from math import sqrt

def pontosTime1(x):
    return 25*x

def pontosTime2(x):
    return 22*x

pontosx = 0
pontosy = 0

for i, line in enumerate(stdin):
    if i == 0:
        pontosx = pontosTime1(int(line))
    if i == 1:
        pontosx += pontosTime1(int(line))
    if i == 2:
        pontosy = pontosTime2(int(line))
    if i == 3:
        pontosy += pontosTime2(int(line))

if pontosx > 10:
    pontosx = 10*3 + (pontosx-10)*2
else:
    pontosx = pontosx*3

if pontosy > 16:
    pontosy = 16*3 + (pontosy-16)*2
else:
    pontosy = pontosy*3

pontuacao = ""+str(pontosx)+"-"+str(pontosy)
if pontosx > pontosy:
    print("X Venceu")
elif pontosy > pontosx:
    print("Y Venceu")
else:
    print("Empate")

print(pontuacao)