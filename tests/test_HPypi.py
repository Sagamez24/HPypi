import unittest
import pandas as pd
from desoper.HPypi import solucion_total


#class Test_hello(unittest.TestCase):
 #   def test__working(self):
  #      self.assertEqual(1,1, True)
#self.assertEqual(HPypi.hello(),
 #                        'Hello, World!', True)

class Test_hello(unittest.TestCase):
    def test__working1(self):
        ls1=solucion_total(5,9,400000,30,0)
        self.assertEqual(12,ls1.shape[0], True)

    def test__working2(self):
        ls2=solucion_total(6,9,400000,30,0)
        self.assertEqual(141,ls2.shape[0], True)
            
if __name__ == '__main__':
    unittest.main()
