import sys
import argparse
import Commandline as CM
        
    

if __name__ == "__main__":


    cm = CM.Commandline(sys.argv[1:])
        
    parser = argparse.ArgumentParser()
    
    subparsers = parser.add_subparsers(help='commands')

    # EC (Elliptic curve) parameter manipulation and generation
    ecparam = subparsers.add_parser('ecparam', 
            help='EC parameter manipulation and generation')
    
    # ecparam options
    ecparam.add_argument('-list_curves', 
            help="Prints a list of all currently available curve 'short names'",
            action="store_true")
    
    ecparam.add_argument('-name', type=str, nargs=1, 
            help="Use the ec parameters with 'short name' name",
            metavar=('arg'))
    
    ecparam.add_argument('-genkey',
            help="Generate ec key",
            action="store_true")
    
    ecparam.add_argument('-out', type=str, nargs=1,
            help="output file",
            metavar=('arg'))


    # Encrypt 
    encrypt = subparsers.add_parser('encrypt', help='Encrypt text or document')
    
    # encrypt options
    encrypt.add_argument('-name', type=str, nargs=1, 
            help="Use the ec parameters with 'short name'", metavar=('arg'))
    encrypt.add_argument('-key', type=str, nargs=1, 
            help="Specifies the input key file", metavar=('arg'))
    encrypt.add_argument('-out', type=str, nargs=1 ,
            help="output file", metavar=('arg'))
    encrypt.add_argument('-text', 
            help="Enter the message to encrypt", action="store_true")
    encrypt.add_argument('-input', type=str, nargs=1, 
            help="Specifies the input document file", metavar=('arg'))
    
    # decrypt 
    decrypt = subparsers.add_parser('decrypt', help='Decrypt document')
    
    decrypt.add_argument('-key', type=str, nargs=1, 
            help="Specifies the input key file", metavar=('arg'))
    decrypt.add_argument('-out', type=str, nargs=1 ,
            help="output file", metavar=('arg'))
    decrypt.add_argument('-input', type=str, nargs=1, 
            help="Specifies the input document file", metavar=('arg'))

    args = parser.parse_args()
    
    cm.run(args)

