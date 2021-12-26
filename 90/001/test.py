import sys
import unittest
from io import StringIO


def cutter(K, pieces, min_length):
    # print(f'cutter {K=} {pieces=} {min_length=}')
    num_pieces = 0
    shorter_len = 0
    for l in pieces:
        if shorter_len + l >= min_length:
            # print(f'then {shorter_len=} {l=} {min_length=}')
            num_pieces = num_pieces + 1
            shorter_len = 0
        else:
            # print(f'else {shorter_len=} {l=} {min_length=}')
            shorter_len = shorter_len + l
    # print(f'{num_pieces=} {K + 1=}')
    if num_pieces >= K + 1:
        return min_length
    else:
        return 0


def resolve():
    N, L = map(int, input().split(' '))
    K = int(input())
    As = list(map(int, input().split(' ')))

    # print(f'{len(As)=}')

    tmp_list = [0] + As + [L]
    pieces = [tmp_list[a + 1] - tmp_list[a] for a in range(len(tmp_list) - 1)]

    # print(f'{N=} {L=} {K=} {As=} {pieces=}')

    right = 0
    left = L

    results = []

    while left - right > 1:
        min_length = (right + left) // 2
        # print(f'before {min_length=} {right=} {left=}')
        if (result := cutter(K, pieces, min_length)):
            # print(f'then {min_length=} {right=} {left=}')
            results.append(result)
            right = min_length
        else:
            # print(f'else {min_length=} {right=} {left=}')
            left = min_length

    print(f'{max(results)}')


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):

        self.maxDiff = None

        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 34
1
8 13 26"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 45
2
7 11 16 20 28 34 38"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 100
1
28 54 81"""
        output = """46"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3 100
2
28 54 81"""
        output = """26"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954"""
        output = """170"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
