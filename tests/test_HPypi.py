import unittest
import pandas as pd
from desoper.HPypi import solucion_total


#class Test_hello(unittest.TestCase):
 #   def test__working(self):
  #      self.assertEqual(1,1, True)
#self.assertEqual(HPypi.hello(),
 #                        'Hello, World!', True)

class Test_solucion_total(unittest.TestCase):
	   def test_n5(self):
	      sls_5 = solucion_total(5,9,10000,30,0)
	      self.assertEqual(11, sls_5.shape[0], True)                                
	                        
	   def test_n6(self):
	      sls_6 = solucion_total(6,9,500000,30,0)
	      self.assertEqual(112, sls_6.shape[0], True)
            
if __name__ == '__main__':
    unittest.main()
