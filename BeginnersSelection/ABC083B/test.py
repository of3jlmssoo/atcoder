import sys
import unittest
from io import StringIO


def resolve():  # (N, A, B):
    N, A, B = input().split(' ')

    N = int(N)
    A = int(A)
    B = int(B)
    result = 0
    for x in range(N + 1):
        tmp_result = 0
        for y in str(x):
            tmp_result = tmp_result + int(y)
        if tmp_result >= A and tmp_result <= B:
            result = result + x
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
        input = """20 2 5"""
        output = """84"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 1 2"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 4 16"""
        output = """4554"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
    # resolve(20, 2, 5)
    # resolve(10, 1, 2)
    # resolve(100, 4, 16)
