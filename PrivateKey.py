import os
import base64

class PrivateKey(object):
    __key__ = None



    def generateKey(self, size = 256):
        key = os.urandom(size)
        key = base64.b64encode(key)

        self.__key__ = key

        return key



    def getKey(self):
        return self.__key__


    def printKey(self):
        key = self.getKey()


        keyparse = '-----BEGIN EC PRIVATE KEY-----\n{}\n-----END EC PRIVATE KEY-----'.format(key.decode('utf8'))


        return keyparse





