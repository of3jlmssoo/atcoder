import subprocess
from unittest import TestCase, main


class MyTestClass(TestCase):
    def _std_test(self, param):
        p = subprocess.Popen(
            ['python', 'main.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        o, e = p.communicate(input=param[0].encode())
        if o.decode().strip() != str(param[1]):
            print(o.decode())
        self.assertEqual(e.decode(), "")
        self.assertEqual(o.decode().strip(), str(param[1]))

    def test_case(self):
        """
        標準入力するものや期待される標準出力はダミーデータです
        """
        params = (
            ("1\n2 3\ntest", "6 test"),
            ("72\n128 256\nmyonmyon", "456 myonmyon")
        )

        for param in params:
            with self.subTest(param=param):
                self._std_test(param)


mytest = MyTestClass()
mytest.test_case()
