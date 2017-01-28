import os
import base64

class PublicKey(object):
    """
    Generates a 256-bit public key and convert to base64
    """

    def generateKey(self, size = 256):
        key = os.urandom(size)
        key = base64.b64encode(key)
    

        return key


    def extractKey(self,key):
        key = key.decode('utf-8')
        key = key.splitlines()
        key = base64.b64decode(key[1])
        key = int.from_bytes(key, byteorder='big')
        
        return key


    def printKey(self, key):

        keyparse = '-----BEGIN EC PUBLIC KEY-----\n'
        keyparse += '{}\n-----END EC PUBLIC KEY-----'.format(key.decode('utf8'))


        return keyparse

