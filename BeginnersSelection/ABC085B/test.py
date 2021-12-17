import sys
import unittest
from io import StringIO


def resolve():
    N = int(input())
    mochi = [0] * N
    for x in range(N):
        mochi[x] = int(input())
    mochi = sorted(mochi, reverse=True)
    result = []

    for x in mochi:
        if not len(result):
            result.append(x)
            continue

        if x < result[-1]:
            result.append(x)
            continue

    print(len(result))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4
10
8
8
6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
15
15
15"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
50
30
50
100
50
80
30"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
