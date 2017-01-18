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

    def test_EC(self):
        with self.assertRaises(Exception) as context:
            p = pri.Prime(13)
            ec = EC.EllipticCurve(0, 0, p)


        excep = 'The curve is not valid!'

        self.assertTrue(excep in str(context.exception))


    def test_ECPoint(self):
        p  = pri.Prime(13)
        ec = EC.EllipticCurve(3, 8, p)
        
        with self.assertRaises(Exception) as context:
            pFail = ec.pointTest(20, 23)

        
        excep = 'Coordinates must be less than the prime'

        self.assertTrue(excep in str(context.exception))




        self.assertTrue(ec.pointTest(1, 5))
        self.assertTrue(ec.pointTest(1, 8))
        self.assertFalse(ec.pointTest(0, 11))

if __name__ == '__main__':
    unittest.main()
