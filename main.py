import sys
import argparse
import Commandline as CM
import CurveDB     as DB
import PrivateKey  as PK


if __name__ == "__main__":


    cm = CM.Commandline(sys.argv[1:])
        
    parser = argparse.ArgumentParser()
    
    subparsers = parser.add_subparsers(help='commands')

    # EC (Elliptic curve) parameter manipulation and generation
    ecparam = subparsers.add_parser('ecparam', help='EC parameter manipulation and generation')
    
    # ecparam options
    ecparam.add_argument('-list_curves', help="Prints a list of all currently available curve 'short names'", action="store_true")
    ecparam.add_argument('-name', type=str, nargs=1, help="Use the ec parameters with 'short name' name'", metavar=('arg'))
    ecparam.add_argument('-genkey', help="Generate ec key'", action="store_true")
    ecparam.add_argument('-out', type=str, nargs=1 , help="output file'", metavar=('arg'))


    # Encrypt 
    ecnrypt = subparsers.add_parser('encrypt', help='Encrypt text or document')



    args = parser.parse_args()
    
    cm.run()

    
    db = DB.CurveDB()
    
    if args.list_curves:
        db.printDB()
    if args.name:
        curve = args.name[0]
        db.printCurve(curve)
    if args.genkey:
        pk = PK.PrivateKey()
        pk.generateKey()
        pk.printKey()
    if args.out:
        print("output file")


