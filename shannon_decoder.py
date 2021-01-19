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
            break

        head = head + 1
        ahead = ahead + 1
    print("Dictionary is received\n")
    return mydict, head, ahead


def getText(head, file):
    print("Decoding text...\n")
    binaryText = file[head:(len(file))]
    text = ''
    for char in binaryText:
        text += bin(ord(chr(char)))[2:].zfill(7)

    return text


def getDecodedText(text, mydict):
    letter = ""
    searchb = 0
    searchIterator = 0
    while searchb in range(len(text)):
        searchBuffer = text[searchIterator:searchb]
        stringBuffer = searchBuffer

        if stringBuffer in mydict:
            letter += str(mydict[stringBuffer])
            searchIterator = searchb;

        searchb = searchb + 1
    print("Text has been decoded\n")
    return letter


def dict2File(file):
    bytes = zlib.decompress(file)
    return pickle.loads(bytes)


def writeToFile(file, letter):
    print("Writing decoded text to file...\n")
    array = []
    a = 0
    while a in range(len(letter)):
        while len(array) < 8 and a < len(letter):
            array.append(int(letter[a]))
            a = a+1
        char = bytearray(numpy.packbits(array)).decode('latin1')
        byte = bytes(char, 'latin1')
        file.write(byte)
        array.clear()
    print("Writing to file is done\n")
    return file


main()