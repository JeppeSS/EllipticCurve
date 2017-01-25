import os
import base64

class PrivateKey(object):

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

        keyparse  = '-----BEGIN EC PRIVATE KEY-----\n'
        keyparse += '{}\n-----END EC PRIVATE KEY-----'.format(key.decode('utf8'))


        return keyparse

