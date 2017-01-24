import sys
import CurveDB     as DB
import PrivateKey  as PK
import Filemanager as FM

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


        data = ""


        if args.list_curves:
            data = db.printDB()
        
        if args.name:
            curveName = args.name[0]
            data      = db.printCurve(curveName)

        if args.genkey:
            pk = PK.PrivateKey()

            pk.generateKey()

            data = pk.printKey()


        if args.out:
            fm.writeOut(data, args.out[0])
        else:
            print(data)

        
    
