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

curve3 = ['brainpoolP224r1', 'RFC 5639 curve over a 224 bit prime field',
        0X68A5E62CA9CE6C1C299803A6C1530B514E182AD8B0042A59CAD29F43,
        0X2580F63CCFE44138870713B1A92369E33E2135D266DBB372386C400B,
        0XD7C134AA264366862A18302575D1D787B09F075797DA89F57EC8C0FF,
        (0X0D9029AD2C7E5CF4340823B2A87DC68C9E4CE3174C1E6EFDEE12C07D,
            0X58AA56F772C0726F24C6B89E4ECDAC24354B9E99CAA3F6D3761402CD)
        ]

curve4 = ['brainpoolP256r1', 'RFC 5639 curve over a 256 bit prime field',
       0X7D5A0975FC2C3057EEF67530417AFFE7FB8055C126DC5C6CE94A4B44F330B5D9,
       0X26DC5C6CE94A4B44F330B5D9BBD77CBF958416295CF7E1CE6BCCDC18FF8C07B6,
       0XA9FB57DBA1EEA9BC3E660A909D838D726E3BF623D52620282013481D1F6E5377,
       (0X8BD2AEB9CB7E57CB2C4B482FFC81B7AFB9DE27E1E3BD23C23A4453BD9ACE3262
,0X547EF835C3DAC4FD97F8461A14611DC9C27745132DED8E545C1D54C72F046997)
        ]

curve5 = ['brainpoolP320r1', 'RFC 5639 curve over a 320 bit prime field',       0X3EE30B568FBAB0F883CCEBD46D3F3BB8A2A73513F5EB79DA66190EB085FFA9F492F375A97D860EB4,    0X520883949DFDBC42D3AD198640688A6FE13F41349554B49ACC31DCCD884539816F5EB4AC8FB1F1A6, 0XD35E472036BC4FB7E13C785ED201E065F98FCFA6F6F40DEF4F92B9EC7893EC28FCD412B1F1B32E27, (0X43BD7E9AFB53D8B85289BCC48EE5BFE6F20137D10A087EB6E7871E2A10A599C710AF8D0D39E20611
,0X14FDD05545EC1CC8AB4093247F77275E0743FFED117182EAA9C77877AAAC6AC7D35245D1692E8EE1)
        ]

db.registerCurve(curve)
db.registerCurve(curve2)
db.registerCurve(curve3)
db.registerCurve(curve4)
db.registerCurve(curve5)

