from sys import stdin

def int_from_base(s,b):
    return int(s,b)

def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def int_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

filas = [] # (base,n,f)

onfila = 0
base = 0
n = ''
f = ''
for i, line in enumerate(stdin):
    if onfila == 0:
        base = int(line)
        if base == 0:
            break
        onfila = 1
    elif onfila == 1:
        n = line.replace(' ', '').replace('\n', '').upper()
        onfila = 2
    elif onfila == 2:
        f = line.replace(' ', '').replace('\n', '').upper()
        filas.append((base, n, f))
        onfila = 0

for b,n,f in filas:
    v1 = int_from_base(n,b)
    v2 = int_from_base(f,b)
    sum = int_to_base(int_from_base(f, b) + int_from_base(n, b), b)
    result = ''.join([digit_to_char(d) for d in sum])
    print(result.upper())
