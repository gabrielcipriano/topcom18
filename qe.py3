from sys import stdin

n_alunos = 0
n_grupos1 = 0
n_grupos2 = 0

groups1 = []
groups2 = []

for i, line in enumerate(stdin):
    try:
        linha = line.split()

        if i == 0:
            n_alunos = int(linha[0])
            n_grupos1 = int(linha[1])
            n_grupos2 = int(linha[2])
            continue

        if i <= n_grupos1:
            groups1.append((linha[0], linha[1]))
        else:
            groups2.append((linha[0], linha[1]))
    except:
        continue

grupos1 = set(groups1)
grupos2 = set(groups2)

if grupos1.intersection(grupos2):
    print(0)
else:
    print(1)