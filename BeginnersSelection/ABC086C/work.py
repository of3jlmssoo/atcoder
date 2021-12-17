""" [summary]
2
3 1 2   時間移動量3 実移動量 1-0  +  2 - 0 = 1+2 = 3
6 1 1   時間移動量3 実移動量 1-1  +  |1-2| = 0+1 = 1   時間移動量 = 実移動量 or 時間移動量 = 実移動量x2の倍数

0       1       2       3       4     5     6
(0,0), (0,1), (1,1), (1,2), (1,1), (1,0), (1,1)


    0   0,0     0,0     0,0
    1   1,0     1,0     0,1
    2   0,0     2,0     0,0
    3   1,0     1,0     0,1
    4   0,0     2,0     0,0

"""


def resolve(*travel_info):
    # print(f'{travel_info=}')
    cur_t = 0
    cur_x = 0
    cur_y = 0
    result = 'No'
    for travel in travel_info:
        t, x, y = travel.split(' ')
        t = int(t)
        x = int(x)
        y = int(y)
        print(f'{t=} {x=} {y=}')
        t_val = t - cur_t
        x_val = abs(x - cur_x)
        y_val = abs(y - cur_y)
        print(f'{t_val=} {x_val=} {y_val=}')

        if t_val == x_val + y_val:
            result = 'Yes'

        xy_val = x_val + y_val
        print(f'{x_val=}  {y_val=} {xy_val=} {t_val=} {t_val%2=}')
        if xy_val != 0:
            if not t_val % (x_val + y_val):
                result = 'Yes'
        elif t_val % 2:
            result = 'No'
        else:
            result = 'Yes'

        if result == 'Yes':
            cur_t = t
            cur_x = x
            cur_y = y

        if result == 'No':
            break

    print(result)


resolve('3 1 2', '6 1 1')
print('\n')
resolve('2 100 100')
print('\n')
resolve('5 1 1', '100 1 1')
print('\n')
resolve('1 2 2')
print('\n')
resolve('1 0 0')
print('\n')
resolve('2 0 0')
