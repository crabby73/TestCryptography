from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
from argparse import ArgumentParser
from caesar_encryption import encryptText, decryptText
from file_operations import readInputFile, writeOutputFile
import string

parser = ArgumentParser()

parser.add_argument("-f", "--file", dest="infile", default="none")
parser.add_argument("-o", "--operation", dest="operation", default="encode")
parser.add_argument("-k", "--key", dest="key", type=int, default=0)

args = parser.parse_args()

key = os.urandom(16)
aesCipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()


# Check if input string can be devided by 16
# If yes continue
# If not add missing bytes
# Add 16 bytes blocks that contains information about number of padding bytes
def adaptBlockSizeOfInputText(text) -> string:

    rest = len(text) % 16
    if rest != 0:

    return ""


# Do encryption of resulting string

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

    # print(outText)
    writeOutputFile(outText)

elif args.infile != "none" and args.operation == "decode":
    outText = list()
    inText = readInputFile(args.infile)
    for line in inText:
        decryptedLine = decryptText(line, args.key)
        outText.append(decryptedLine)

    # print(outText)
    writeOutputFile(outText)
else:
    print("I do not yet work like this.")
