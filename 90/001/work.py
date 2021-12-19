"""
分割する(短いピースに着目する)
規定回数=規定回数+1
分割後をlong_oneとshort_oneにセットする
if 規定回数に達しているか？
  return なんとかかんとか(短い方、long_one、short_one)
long_oneで再帰コール(return will be p1, l1, s1)
short_oneで再帰コール(return will be p2, l2, s2)
(l1,s1)の短い方と(l2,s2)の短い方を比較して長い方を選択
"""
tup_NL = (3, 34)
tup_K = (1)
tup_As = (8, 13, 26)


def resolve():
    N = tup_NL[0]
    L = tup_NL[1]
    K = tup_K
    A = list(tup_As)

    pieces = [0] + A + [L]
    # print(pieces)
    print(cut_jcake(L, K, pieces))


def prepare_cut():
    pass


def cut_jcake(L, K, A):
    """cut_jcake

    Args:
        L ([type]): ケーキの長さ
        K ([type]): K回切る
        A (list): 切る位置
    """
    print(L, K, A)
    pieces = [A[p + 1] - A[p] for p in range(len(A) - 1)]
    print(pieces)
    mins = [i for i, j in enumerate(pieces) if j == min(pieces)]
    print(mins)
    result = 0
    for m in mins:
        if mins == 0:
            pass
        if mins == len(pieces) - 1:
            pass


resolve()
