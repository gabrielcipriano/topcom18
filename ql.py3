
if __name__ == '__main__':
    g = int(input())
    set_ = set()
    for i in range(g):
        _, *amigos = map(int, input().split())
        amigos = set(amigos)
        if i == 0:
            set_.update(amigos)
        else:
            set_.intersection_update(amigos)

        if len(set_) == 0:
            print("IMPOSSIVEL!")
            exit()
        
    print("{} amigos em comum!".format(len(set_)))

