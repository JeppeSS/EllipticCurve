import Point as PO
import os
import base64

class ElGamal(object):

    __curve__ = None
    __point__ = None
    __prime__ = None



    def __init__(self, curve, point):

        self.__curve__ = curve
        self.__point__ = point
        self.__prime__ = curve.getPrime()



    def partition(self, data, length):
        return [data[i:i + length] for i in range(0, len(data), length)] 
    
    def getPrime(self):
        return self.__prime__

    def getPoint(self):
        return self.__point__


    def getCurve(self):
        return self.__curve__


    def genRandom(self):
        num = os.urandom(256)

        return int.from_bytes(num, byteorder='big')
    
    
    def legendre(self, a, p):
        return pow(a, (p - 1) // 2, p)
     
    def tonelli(self, n, p):
        if self.legendre(n, p) != 1:
            return 0

        q = p - 1
        s = 0
        while q % 2 == 0:
            q //= 2
            s += 1
        if s == 1:
            return pow(n, (p + 1) // 4, p)
        for z in range(2, p):
            if p - 1 == self.legendre(z, p):
                break
        c = pow(z, q, p)
        r = pow(n, (q + 1) // 2, p)
        t = pow(n, q, p)
        m = s
        t2 = 0
        while (t - 1) % p != 0:
            t2 = (t * t) % p
            for i in range(1, m):
                if (t2 - 1) % p == 0:
                    break
                t2 = (t2 * t2) % p
            b = pow(c, 1 << (m - i - 1), p)
            r = (r * b) % p
            c = (b * b) % p
            t = (t * c) % p
            m = i
        return r



   

    def encrypt(self, data, key, curveName):


        data      = list(data)
        prime     = self.getPrime()
        primeSize = prime.bit_length()
        curve     = self.getCurve()


        M         = int((primeSize - 8) / 8)
        
        partition = self.partition(data, M)


        binaryData = [] 
        for index in partition:
            binaryData.append([bin(x)[2:].zfill(8) for x in index])

        
        lengthBinary = len(binaryData[-1])
 
        while lengthBinary < M:
            binaryData[-1].append('00000000')
            lengthBinary = len(binaryData[-1])

 
        
        sample = []
        for index in binaryData:
            index.append('00000000')
            
            asString = ''.join(index)

            sample.append(asString)


        toInt = []
        for i in sample:
            toInt.append(int(i, 2))


        points = []
        for index in toInt:
            y = curve.calcPos(index)
            test = self.tonelli(y, prime)
            
            while test == 0: 
                index += 1
                index = index % prime

                y = curve.calcPos(index)
                test = self.tonelli(y, prime)

            if curve.pointTest(index, test):
                p = PO.Point(curve, index, test)
                points.append(p)



        point  = self.getPoint()
        random = self.genRandom()

        pB  = point.double_and_add(key)
        c1  = point.double_and_add(random)
        kpB = pB.double_and_add(random)
        
        c2 = []
        for i in points:
             c2.append(kpB.add(i))

 
        c1 = '{}:{}'.format(c1.getX(), c1.getY())
        c1 = base64.b64encode(str.encode(c1))

        curveName = base64.b64encode(str.encode(curveName))
        param  = '-----BEGIN EC CURVENAME-----\n'
        param += '{}\n-----END EC CURVENAME-----\n\n'.format(curveName.decode('utf8'))
        
        param += '-----BEGIN EC PARAMETERS-----\n'
        param += '{}\n-----END EC PARAMETERS-----\n\n'.format(c1.decode('utf8'))


        c2Param = '-----BEGIN EC MESSAGE-----\n'
        for i in c2:
            c2Format = '{}:{}'.format(i.getX(), i.getY())
            c2Format = base64.b64encode(str.encode(c2Format))
            c2Param += '{}\n'.format(c2Format.decode('utf8'))

        c2Param += '-----END EC MESSAGE-----\n'

        param += c2Param
         

        return param


    def decrypt(self, data, key):
        
        curve = self.getCurve()

        c1 = base64.b64decode(data[1])
        c1 = c1.decode()
        c1 = c1.split(":")
        
        c1    = PO.Point(curve, int(c1[0]), int(c1[1]))
        c1Key = c1.double_and_add(key)
        
        length = len(data)
        msg    = data[5: length - 1]
        
        
        prime       = self.getPrime()
        primelength = prime.bit_length()

        bitSize = "{0:0%sb}" % primelength
        
        decode = []
        for i in msg:
            p = base64.b64decode(i)
            decode.append(p.decode())

        
        points = []
        for i in decode:
            p = i.split(":")
            points.append(PO.Point(curve, int(p[0]), int(p[1])))

       

        p2 = c1Key.__inv__()

        pointsCalc = []
        for i in points:
            pointsCalc.append(i.add(p2))

        binaryN = []
        for i in pointsCalc:
            x = i.getX()
            
            binary = bitSize.format(x)[:-8]

            binaryN.append(binary)


        samp = ''.join(binaryN)
        

        parti = (self.partition(samp, 8))
        
        toStr = []        
        for i in parti:
            toInt = int(i, 2)
            toStr.append(chr(toInt))


        while toStr[-1] == '\x00':
            del toStr[-1]
        

        return ''.join(toStr)


