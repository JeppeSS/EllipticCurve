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




