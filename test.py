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


    def test_EC_PointAdd(self):
        p  = pri.Prime(13)
        ec = EC.EllipticCurve(3, 8, p)

        point1 = Point.Point(ec, 1, 5)
        point2 = Point.Point(ec, 1, 8)
        point3 = Point.Point(ec, 2, 3)
        point4 = Point.Point(ec, 2, 10)
        point5 = Point.Point(ec, 9, 6)
        point6 = Point.Point(ec, 9, 7)
        point7 = Point.Point(ec, 12, 2)
        point8 = Point.Point(ec, 12, 11)
        
        with self.assertRaises(Exception) as context:
            pFail = point1.add(point2)

        
        excep = 'If x1 == x2 the point does not exist'

        self.assertTrue(excep in str(context.exception))


        self.assertEqual(point1.add(point1), point4)
        self.assertEqual(point1.add(point3), point2)
        self.assertEqual(point1.add(point4), point6)
        self.assertEqual(point1.add(point5), point3)
        self.assertEqual(point1.add(point6), point7)
        self.assertEqual(point1.add(point7), point8)
        self.assertEqual(point1.add(point8), point5)


    def test_doubleAndAdd(self):
        p     = pri.Prime(3623)
        ec    = EC.EllipticCurve(14, 19, p)
        point = Point.Point(ec, 6, 730)
        result = Point.Point(ec, 3492, 60)

        self.assertEqual(point.double_and_add(947), result)


if __name__ == '__main__':
    unittest.main()
