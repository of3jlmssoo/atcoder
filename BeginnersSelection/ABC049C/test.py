import sys
import unittest
from io import StringIO


def resolve():
    s = input()
    targets = ['dream', 'dreamer', 'erase', 'eraser']
    min_len = 5

    current_len = len(s)
    while current_len >= min_len:
        for t in targets:
            if t == s[- len(t):]:
                s = s[0: - len(t)]
        if current_len == len(s) or current_len == 0:
            break
        current_len = len(s)

    if current_len > 0:
        print('NO')
    else:
        print('YES')


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
        input = """erasedream"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """dreameraser"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """dreamerer"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
