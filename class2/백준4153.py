while True:
        n = list(map(int, input().split()))
        max_n = max(n)
        if sum(n) == 0:
                break
        n.remove(max_n)
        if n[0] ** 2 + n[1] ** 2 == max_n ** 2:
                print('right')
        else:
                print('wrong')