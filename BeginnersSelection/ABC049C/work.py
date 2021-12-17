
def resolve(s):
    targets = ['dream', 'dreamer', 'erase', 'eraser']
    min_len = 5

    current_len = len(s)
    while current_len >= min_len:
        for t in targets:
            print(f'{s=} - {t=} {s[ - len(t):]} ', end='')
            if t == s[- len(t):]:
                s = s[0: - len(t)]
            print(f'{s=}')
        if current_len == len(s) or current_len == 0:
            print(f'will bread. {current_len=} {len(s)=}')
            break
        current_len = len(s)

    print(f'{current_len=}')
    if current_len > 0:
        print('NO')
    else:
        print('YES')


resolve('erasedream')
print('\n')
resolve('dreameraser')
print('\n')
resolve('dreamerer')
