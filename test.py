import Prime as pri
import EllipticCurve as EC
import Point
import unittest



class TestEC(unittest.TestCase):

    def test_prime(self):
        with self.assertRaises(Exception) as context:
            p = pri.Prime(1)
        
        with self.assertRaises(Exception) as context2:
            p2 = pri.Prime(4284238812392)

        
        
        excep = 'The prime is not valid!'

        self.assertTrue(excep in str(context.exception))
        self.assertTrue(excep in str(context2.exception))
        
        
        
        self.assertTrue(pri.Prime(2))
        self.assertTrue(pri.Prime(2))
        self.assertTrue(pri.Prime(15485863))


if __name__ == '__main__':
    unittest.main()
