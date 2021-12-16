import itertools

# import sort

l = [500, 500, 100, 100, 50, 50]
l = [500, 500, 500, 500, 500, 100]
l = [500] * 5 + [100] * 1 + [50] * 0
l = [500] * 30 + [100] * 40 + [50] * 50
expected_result = 6000
result = []
print(f'{l=}')
for u in range(1, len(l) + 1):
    c_list = list(itertools.combinations(l, u))
    # c_list = list(itertools.permutations(l, u))
    # print(f'{c_list=}')
    for v in c_list:
        # print(f'{type(v)=}, {sum(v)=}')
        # if sum(v) == 100:
        if sum(v) == expected_result:
            w = sorted(v)
            if w not in result:
                result.append(w)

print(len(result))
