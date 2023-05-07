from sys import stdin

def transpose(lst):
    return list(map(list, zip(*lst)))

um = ['X','X','X','X','X']

zero  = [
    ['X', 'X', 'X'],
    ['X', '-', 'X'],
    ['X', '-', 'X'],
    ['X', '-', 'X'],
    ['X', 'X', 'X']
]
zero = transpose(zero)


space = ['-', '-', '-', '-', '-']

traco = [['-', '-', 'X', '-', '-'], ['-', '-', 'X', '-', '-'] ]

def painel_limpo():
    return transpose([
        ['-'] * 20,
        ['-'] * 20,
        ['-'] * 20,
        ['-'] * 20,
        ['-'] * 20,
    ])

def build_num(binary):
    num = []
    for b in list(binary):
        if b == '1':
            num.append(um)
        elif b == '0':
            num.extend(zero)
        num.append(space)
    num.extend(traco)
    num.append(space)
    return num

def _join(lst):
    return(''.join(lst))

def print_painel(painel, t):
    t = t+20
    print('||||||||||||||||||||')
    for p in painel:
        print(p[t-20:t])
    print('||||||||||||||||||||')

if __name__ == '__main__':
    bin_, *tempos = stdin
    bin_ = bin_.strip()
    tempos = list(map(int, tempos))


    max_t = max(tempos)

    binPrint = build_num(bin_)

    painel = painel_limpo()

    while len(binPrint) < max_t: 
        binPrint.extend(build_num(bin_))
    
    painel.extend(binPrint)

    painel = transpose(painel)

    painel = list(map(_join, painel))

    for tempo in tempos:
        print_painel(painel, tempo)