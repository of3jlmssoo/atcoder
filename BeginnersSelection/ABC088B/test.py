import sys
import unittest
from io import StringIO


# def resolve(cards):
def resolve():
    N = int(input())
    cards = input().split(' ')
    # cards = cards.split(' ')

    cards = sorted([int(v) for v in cards], reverse=True)
    alice = 0
    bob = 0
    index = 0

    for x, y in enumerate(cards):
        if x % 2:
            bob = bob + y
        else:
            alice = alice + y

    print(alice - bob)


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
3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2 7 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
20 18 2 18"""
        output = """18"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
    # resolve("3 1")
    # resolve("2 7 4")
    # resolve("20 18 2 18")
