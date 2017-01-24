import Filemanager as fm
import Prime as pri
import EllipticCurve as EC
import Point as po
import os


class ElGamal(object):

    __curve__ = None
    __point__ = None
    __prime__ = None
    __data__  = None



    def __init__(self, curve, point, data):

        self.__curve__ = curve
        self.__point__ = point
        self.__prime__ = curve.getPrime()
        self.__data__  = data


    def integerDigits(self, n, b):
        ls = []

        while n > 0:
            x = n % b

            ls.append(x)
            
            n = n // b

        return ls

    def fromDigits(self, ls, b):

        holder = 0

        for i in range(len(ls)):
            holder = holder + ls[i]

            if i != len(ls) - 1:
                holder = holder * b

        return holder


    def partition(self, data, length):
        return [data[i:i + length] for i in range(0, len(data), length)] 
    
    def getPrime(self):
        return self.__prime__

    def getPoint(self):
        return self.__point__


    def genRandom(self):
        num = os.urandom(20)

        return int.from_bytes(num, byteorder='big')

   

    def encrypt(self, data, key):
        n = len(self.integerDigits(self.getPrime(), 6000)) - 1

        data = list(map(int, data))


        data = self.partition(data, n)
    
        bigInt = []
         
        for i in range(len(data)):
            bigInt.append(self.fromDigits(data[i], 6000))

        if len(bigInt) % 2 != 0:
            bigInt.append(32)


        point = self.getPoint()
        random = self.genRandom()


        pB = point.double_and_add(key)
        c1 = point.double_and_add(random)


        kpB = pB.double_and_add(random)
    
        data = self.partition(bigInt, 2)
        

        pC = []

        for i in data:
            pC.append(kpB.sub(i[0], i[1])) 


        return (c1, pC)


    def decrypt(self, data, key):
        point = self.getPoint()
        pB = point.double_and_add(key)

        kG = data[0] 
        pC = data[1]
 
        nBkG = kG.double_and_add(key)
       
        pt = []
        for i in pC:
            pt.append(nBkG.sub2(i[0], i[1], nBkG.getX(), -(nBkG.getY())))
        
        
        ps = []
        for i in pt:
            ps.append(i[0])
            ps.append(i[1])


        final = []
        for i in ps:
            dt = self.integerDigits(i, 6000)
            dt = dt[::-1]
            final.append(dt)
            
        
        flat = [x for sublist in final for x in sublist]

        return flat

        
