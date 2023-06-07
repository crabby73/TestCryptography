import string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def adaptBlockSizeOfInputText(input_text) -> string:

    rest = len(input_text) % 16
    if rest != 0:
        noOfFillingLetters = 16 - rest
        fillingLetters = ''.join('X' for i in range(noOfFillingLetters))
        result_text = input_text + fillingLetters

    return result_text


def removePaddingLetters(input_text) -> string:
    return''


def encryptAES(text_to_encrypt, key) -> bytes:

    aesCipher = Cipher(algorithms.AES(key.encode()), modes.ECB(), backend=default_backend())
    aesEncryptor = aesCipher.encryptor()
    return aesEncryptor.update(adaptBlockSizeOfInputText(text_to_encrypt).encode())


def decyrptAES(text_to_decrypt, key) -> string:

    aesCipher = Cipher(algorithms.AES(key.encode()), modes.ECB(), backend=default_backend())
    aesDecryptor = aesCipher.decryptor()
    result = aesDecryptor.update(text_to_decrypt)
    return result.decode()
