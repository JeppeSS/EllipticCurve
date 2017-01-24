class Filemanager(object):
    

    def readData(self, filename):
        with open(filename, 'rb') as openFile:
            data = openFile.read()

            openFile.close()

        return data


    def writeOut(self, data, filename):
        with open(filename, 'w') as openFile:
            openFile.write(data)

            openFile.close()



    def convertString(self, text):
        return ''.join(chr(i) for i in text)
    

    def convertAscii(self, text):
        return " ".join(str(ord(char)) for char in text)
    




