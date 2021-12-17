import sys
import unittest
from io import StringIO


def resolve():
mods = [0] * int(input())
inputs_list = input().split(' ')
inputs_list = [int(i) for i in inputs_list]
result = 0
while not sum(mods):
    for i, val in enumerate(inputs_list):
        q, mod = divmod(val, 2)
        if mod:
            mods[i] = mod
            print(result)
            break
        inputs_list[i] = q
    result = result + 1
    # print(i)


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
        input = """3
8 12 40"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 6 8 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
382253568 723152896 37802240 379425024 404894720 471526144"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
