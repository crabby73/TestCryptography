from argparse import ArgumentParser
from caesar_encryption import encryptText, decryptText
from file_operations import readInputFile, writeOutputFile

parser = ArgumentParser()

parser.add_argument("-f", "--file", dest="infile", default="none")
parser.add_argument("-o", "--operation", dest="operation", default="encode")
parser.add_argument("-k", "--key", dest="key", type=int, default=0)

args = parser.parse_args()

#print(args.infile)
#print(args.operation)
#print(args.key)

if args.infile == "none" and args.operation == "encode":
    key = int(input('Schlüssel\n'))
    text = input('Texteingabe\n')
    encryptedText = encryptText(text, key)
    print(encryptedText)

elif args.infile != "none" and args.operation == "encode":
    outText = list()
    inText = readInputFile(args.infile)
    for line in inText:
        encryptedLine = encryptText(line, args.key)
        outText.append(encryptedLine)
    
    #print(outText)
    writeOutputFile(outText)

elif args.infile != "none" and args.operation == "decode":
    outText = list()
    inText = readInputFile(args.infile)
    for line in inText:
        decryptedLine = decryptText(line, args.key)
        outText.append(decryptedLine)
    
    #print(outText)
    writeOutputFile(outText)
else:
    print("I do not yet work like this.")