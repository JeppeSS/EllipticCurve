class CurveDB(object):

    __lsCurves__ = []



    def getDB(self):
        return self.__lsCurves__

    
    def getCurve(self, name):
        db = self.getDB()

        for i in range(len(db)):
            if name == db[i][0]:
                return db[i]

        return 0




    def registerCurve(self, curve):
        
        if len(curve) != 6:
            raise Exception('A curve should contain [name, descr, a, b, prime, point]')


        curvename = curve[0]

        db = self.getDB()

        
        if self.getCurve(curvename) != 0:
            raise Exception('The curvename %s is already defined' % curvename)


        db.append(curve)


    def printDB(self):
        db = self.getDB()
        
        curves = ""

        for curve in db:
            curves += '{}: {}\n'.format(curve[0], curve[1])

        return curves

    def printCurve(self, name):
        curve = self.getCurve(name)
        
        if curve == 0:
            raise Exception('The curve %s does not exist' % name)

        
        prime = hex(curve[4])
        a     = hex(curve[2])
        b     = hex(curve[3])
        gX    = hex(curve[5][0])
        gY    = hex(curve[5][1])



        curveData  = "Field Type: Prime-field\n"
        curveData += "Prime:\n"
        curveData += "\t{}\n".format(prime)
        curveData += "A:\n"
        curveData += "\t{}\n".format(a)
        curveData += "B:\n"
        curveData += "\t{}\n".format(b)
        curveData += "Generator:\n"
        curveData += "\t{}\n".format(gX)
        curveData += "\t{}\n".format(gY)
        
        return curveData 








db = CurveDB()

curve = ['brainpoolP160r1', 'RFC 5639 curve over a 160 bit prime field',
        0X340E7BE2A280EB74E2BE61BADA745D97E8F7C300,
        0X1E589A8595423412134FAA2DBDEC95C8D8675E58,
        0XE95E4A5F737059DC60DFC7AD95B3D8139515620F,
        (0XBED5AF16EA3F6A4F62938C4631EB5AF7BDBCDBC3,
            0X1667CB477A1A8EC338F94741669C976316DA6321)
        ]

curve2 = ['brainpoolP192r1', 'RFC 5639 curve over a 192 bit prime field',
        0X6A91174076B1E0E19C39C031FE8685C1CAE040E5C69A28EF,
        0X469A28EF7C28CCA3DC721D044F4496BCCA7EF4146FBF25C9,
        0XC302F41D932A36CDA7A3463093D18DB78FCE476DE1A86297,
        (0XC0A0647EAAB6A48753B033C56CB0F0900A2F5C4853375FD6,
            0X14B690866ABD5BB88B5F4828C1490002E6773FA2FA299B8F)
        ]




db.registerCurve(curve)
db.registerCurve(curve2)

