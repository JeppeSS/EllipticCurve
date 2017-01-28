import base64

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

    def extractCurve(self, data):
        data = data.decode('utf-8')
        data = data.splitlines()

        curvename = base64.b64decode(data[1])
        curvename = curvename.decode()

        return curvename, data[4:]

