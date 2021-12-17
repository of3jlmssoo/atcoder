def resolve(N, Y):
    for a in range(N + 1):
        for b in range(N + 1 - a):
            if 10000 * a + 5000 * b + 1000 * (N - a - b) == Y:
                print(f'{a} {b} {N-a-b}')
                return
    print('-1 -1 -1')


# resolve(9, 45000)
# resolve(20, 196000)
# resolve(1000, 1234000)
resolve(2000, 20000000)
