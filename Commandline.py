import sys
import Point         as PO
import Prime         as PR
import CurveDB       as DB
import PublicKey     as PK
import Filemanager   as FM
import EllipticCurve as EC
import ElGamal       as EL


class Commandline(object):


    __commands__ = None


    def __init__(self, commands = []):
        self.__commands__ = commands


    def __display_syntax__(self, msg = None):

        filename = sys.argv[0]
        
        if msg is not None:
            print('Error: %s' % (msg), file = sys.stderr)

        print("Syntax: %s [command] [flags]" % (filename), file = sys.stderr)
        print(file = sys.stderr)
        print("%s -h to view commands" % (filename), file = sys.stderr)

    def __display_error__(self, msg, raiseErr = False):

        if raiseErr:
            raise Exception(msg)
        else:
            self.__display_syntax__(msg)
            sys.exit(1)


    def __getCmd__(self):
        return self.__commands__


    def run(self, args):
        cmd = self.__getCmd__()

        if len(cmd) < 1:
            self.__display_error__("No command supplied.")

        self.parse(args)
    
    def parse(self, args):
        db = DB.CurveDB()
        fm = FM.Filemanager()
        pk = PK.PublicKey()
        

        cmd = self.__getCmd__()

        data = ""

        
        if cmd[0] == 'ecparam':
        
            if args.list_curves:
                data = db.printDB()
            
            if args.name:
                curveName = args.name[0]
                data      = db.printCurve(curveName)

            if args.genkey:
                key = pk.generateKey()
                data = pk.printKey(key)
        
        if cmd[0] == 'encrypt':
            if args.name:
                curveName = args.name[0]
                curve     = db.getCurve(curveName)

                if curve == 0:
                    self.__display_error__("Invalid Curve")

                a     = curve[2]
                b     = curve[3]
                prime = curve[4]
                gX    = curve[5][0]
                gY    = curve[5][1]
            
            else:
                self.__display_error__("Choose a curve -name 'short name'")

            if args.key:
                keyFile = fm.readData(args.key[0])
                key     = pk.extractKey(keyFile)

            else:
                self.__display_error__("Select a key file -key 'filename'")

            if args.text:
                print("\nEnter the message:\n\n")
                msg = input()
                msg = str.encode(msg)

            if args.input:
                msg = fm.readData(args.input[0])


            prime = PR.Prime(prime)
            ec    = EC.EllipticCurve(a, b, prime)
            point = PO.Point(ec, gX, gY)
            el    = EL.ElGamal(ec, point)

            data  = el.encrypt(msg, key, curve[0])

        if cmd[0] == 'decrypt':
            
            if args.key:
                keyFile = fm.readData(args.key[0])
                key     = pk.extractKey(keyFile)
            else:
                self.__display_error__("Select a key file -key 'filename'")

            if args.input:
                inp = fm.readData(args.input[0])

            
            curveName, msg = fm.extractCurve(inp)
            curve     = db.getCurve(curveName)
            
            a     = curve[2]
            b     = curve[3]
            prime = curve[4]
            gX    = curve[5][0]
            gY    = curve[5][1]

            prime = PR.Prime(prime)
            ec    = EC.EllipticCurve(a, b, prime)
            point = PO.Point(ec, gX, gY)
            el    = EL.ElGamal(ec, point)
            data  = el.decrypt(msg, key)
            
        if args.out:
            fm.writeOut(data, args.out[0])
        else:
            print(data)

        
    
