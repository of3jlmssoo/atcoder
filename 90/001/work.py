lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""
"""
low = 0
high = len(lst) - 1

mid = int(low + (high - low) / 2)

target = 5

for i in range(len(lst)):
    # print(i)
    low = 0
    high = len(lst) - 1
    mid = int(low + (high - low) / 2)
    target = i
    # print(f'{target=} {mid=} {lst[target]=}')  # , end='')
    while mid != lst[target]:
        # print(f'{mid}')
        if lst[target] < lst[mid]:
            # print(f'then')
            high = mid
        elif lst[target] > lst[mid]:
            # print(f'elif {lst[target]=} {lst[mid]=} {mid=} {target=} {lst[mid + 1]=} {lst[target]=}')
            low = mid
        if lst[mid + 1] == lst[target]:
            # print(f'else')
            mid = mid + 1
            pass
            break
        mid = int(low + (high - low) / 2)
    print(f'{target=} {lst[mid]=} {mid=} ')
