import string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def adaptBlockSizeOfInputText(inputText) -> string:

    rest = len(inputText) % 16
    if rest != 0:
        noOfFillingLetters = 16 - rest
        fillingLetters = ''.join('X' for i in range(noOfFillingLetters))
        resultText = inputText + fillingLetters

    return resultText


def encryptAES(textToEncrypt, key) -> string:

    aesCipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    aesEncryptor = aesCipher.encryptor()
    return aesEncryptor.update(adaptBlockSizeOfInputText(textToEncrypt))


def decyrptAES(textToDecrypt, key) -> string:

    aesCipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    aesDecryptor = aesCipher.decryptor()
    return aesDecryptor.update(textToDecrypt)