from argparse import ArgumentParser
from caesar_encryption import encryptText, decryptText
from file_operations import readFileInOneBlock, writeFileInOneBlock


parser = ArgumentParser()

parser.add_argument("-f", "--file", dest="infile", default="none")
parser.add_argument("-o", "--operation", dest="operation", default="encode")
parser.add_argument("-k", "--key", dest="key", type=int, default=0)

args = parser.parse_args()


if args.infile == "none" and args.operation == "encode":
    key = int(input('Schlüssel\n'))
    text = input('Texteingabe\n')
    encryptedText = encryptText(text, key)
    print(encryptedText)

elif args.infile != "none" and args.operation == "encode":
    outText = list()
    inText = readFileInOneBlock(args.infile)
    for line in inText:
        encryptedLine = encryptText(line, args.key)
        outText.append(encryptedLine)

    # print(outText)
    writeFileInOneBlock(outText)

elif args.infile != "none" and args.operation == "decode":
    outText = list()
    inText = readFileInOneBlock(args.infile)
    for line in inText:
        decryptedLine = decryptText(line, args.key)
        outText.append(decryptedLine)

    # print(outText)
    writeFileInOneBlock(outText)
else:
    print("I do not yet work like this.")
