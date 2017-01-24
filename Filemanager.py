class Filemanager(object):
    

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


            openFile.close()


    def writeOut(self, data, filename):
        with open(filename, 'w') as openFile:
            openFile.write(data)

            openFile.close()


    def readKey(self, filename):
        with open(filename, 'rb') as openFile:
            data = list(openFile.read())

            openFile.close()

            print(data)


    def convertString(self, text):
        return ''.join(chr(i) for i in text)
    

    def convertAscii(self, text):
        return " ".join(str(ord(char)) for char in text)
    


