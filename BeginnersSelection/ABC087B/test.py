import itertools
import sys
import unittest
from io import StringIO


def resolve():
    five_hunred = int(input())
    one_hundred = int(input())
    half_hundred = int(input())
    expected_total = int(input())

    result = 0
    for f in range(five_hunred + 1):
        for o in range(one_hundred + 1):
            for h in range(half_hundred + 1):
                if 500 * f + 100 * o + 50 * h == expected_total:
                    result = result + 1
    print(result)


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
        input = """2
2
2
100"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1
0
150"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
40
50
6000"""
        output = """213"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
