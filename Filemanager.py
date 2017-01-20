class Filemanager(object):
    
    __filename__ = None
    __data__     = None

    def __init__(self, filename):
        self.__filename__ = filename

        self.__data__ = self.readData()
        

    def readData(self):
        with open(self.getFilename(), 'r') as openFile:
            data = list(openFile.read())

            openFile.close()

            data = self.convertAscii(data)

        return data.split()

    def writeData(self, data, name):
        with open(name + '.txt', "w") as openFile:
            data = self.convertString(data)
            openFile.write(data) 


    def convertString(self, text):
        return ''.join(chr(i) for i in text)
    

    def convertAscii(self, text):
        return " ".join(str(ord(char)) for char in text)
    


    def getFilename(self):
        return self.__filename__

    def getData(self):
        return self.__data__


