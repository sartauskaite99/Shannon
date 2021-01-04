import json
import sys
import numpy

def main():
    mydict = None
    
    fileToWrite = sys.argv[2]
    fileToRead = sys.argv[1]
    file = open(fileToWrite, "wb")
    fileRead = open(fileToRead, "rb")
    data = fileRead.read()
    head = 2
    ahead = 0
    dictInterval = 0
    while mydict is None:
        search = data[ahead:head]
        search = search.decode('utf-8')

        if search == '\n\n':
            mydict = data[dictInterval:head]
            mydict = json.loads(mydict)
            print(mydict)
            break
        head = head + 1
        ahead = ahead + 1

    searchIterator = head
    array = []
    while head in range(len(data)+1):
        searchBuffer = data[searchIterator:head]
        stringBuffer = searchBuffer.decode()

        if stringBuffer in mydict:
            print(mydict[stringBuffer])
            letter = str(mydict[stringBuffer])
            for a in letter:
                array.append(int(a))
            letter = bytearray(numpy.packbits(array)).decode('latin1')
            print(letter)
            byte = bytes(letter, 'latin1')
            file.write(byte)
            array.clear()
            searchIterator = head;

        head = head + 1

    fileRead.close()
    file.flush()
    file.close();


main()