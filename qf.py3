
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        expression = input().split('and')
        dict_ = {}
        flag = False
        for item in expression:
            str_ = item.strip()
            if str_.startswith('not'):
                var = str_[4:]
                if var in dict_ and dict_[var] == 1:
                    print("trivialmente falsa")
                    flag = True
                    break
                else:
                    dict_[var] = 0
            else:
                var = str_
                if var in dict_ and dict_[var] == 0:
                    print("trivialmente falsa")
                    flag = True
                    break
                else:
                    dict_[var] = 1
        if not flag:
            print("nem trivialmente verdadeira, nem trivialmente falsa")
