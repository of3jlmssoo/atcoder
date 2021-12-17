import sys
import unittest
from io import StringIO


def resolve():
    N = int(input())
    cur_t = 0
    cur_x = 0
    cur_y = 0
    result = 'Yes'
    for travel in range(N):
        t, x, y = input().split(' ')
        t = int(t)
        x = int(x)
        y = int(y)
        # print(f'{t=} {x=} {y=}')
        t_val = t - cur_t
        x_val = abs(x - cur_x)
        y_val = abs(y - cur_y)

        d = x_val + y_val
        dt = t - cur_t

        if dt < d:
            result = 'No'
            break
        if (dt - d) % 2 == 1:
            result = 'No'
            break
        cur_t = t
        cur_x = x
        cur_y = y

        # print(f'{t_val=} {x_val=} {y_val=}')
        # if t_val == x_val + y_val:
        #     result = 'Yes'

    #     xy_val = x_val + y_val
    #     # print(f'{x_val=}  {y_val=} {xy_val=} {t_val=} {t_val%2=}')
    #     if xy_val != 0:
    #         if not t_val % (x_val + y_val):
    #             result = 'Yes'
    #     elif t_val % 2:
    #         result = 'No'
    #     else:
    #         result = 'Yes'

    #     if result == 'Yes':
    #         cur_t = t
    #         cur_x = x
    #         cur_y = y

    #     if result == 'No':
    #         break

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
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
