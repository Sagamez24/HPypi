import unittest
from desoper import HPypi


class Test_hello(unittest.TestCase):
    def test__working(self):
        self.assertEqual(HPypi.hello(),
                         'Hello, World!', True)


if __name__ == '__main__':
    unittest.main()
