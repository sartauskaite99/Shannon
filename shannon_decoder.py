import sys
import numpy
import zlib
import pickle


def main():
    fileToWrite = sys.argv[2]
    fileToRead = sys.argv[1]

    file = open(fileToWrite, "wb")
    fileRead = open(fileToRead, "rb")

    data = fileRead.read()

    mydict, head, ahead = getDictionary(data)

    text = getText(head, data)

    letter = getDecodedText(text, mydict)

    file = writeToFile(file, letter)
    fileRead.close()
    file.flush()
    file.close();


def getDictionary(file):
    mydict = None
    dictInterval = 0
    head = 2
    ahead = 0
    while mydict is None:
        search = file[ahead:head]
        search = search.decode('latin1')

        if search == '\n\n':
            mydict = file[dictInterval:ahead]
            mydict = dict2File(mydict)
            print(mydict)
            break

        head = head + 1
        ahead = ahead + 1
    return mydict, head, ahead


def getText(head, file):
    binaryText = file[head:(len(file))]
    text = ''

    for char in binaryText:
        text += bin(ord(chr(char)))[2:].zfill(7)
    print(text)

    return text


def getDecodedText(text, mydict):
    letter = ""
    searchb = 0
    searchIterator = 0
    while searchb in range(len(text)):
        searchBuffer = text[searchIterator:searchb]
        stringBuffer = searchBuffer

        if stringBuffer in mydict:
            print(mydict[stringBuffer])
            letter += str(mydict[stringBuffer])
            searchIterator = searchb;

        searchb = searchb + 1

    return letter


def dict2File(file):
    bytes = zlib.decompress(file)
    return pickle.loads(bytes)


def writeToFile(file,letter):
    array = []
    a = 0
    while a in range(len(letter)):
        while len(array) < 8 and a < len(letter):
            array.append(int(letter[a]))
            a = a+1
        print(array)
        char = bytearray(numpy.packbits(array)).decode('latin1')
        print(char)
        byte = bytes(char, 'latin1')
        file.write(byte)
        array.clear()
    return file


main()