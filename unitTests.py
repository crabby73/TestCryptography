import random
import string
from aes_encryption import adaptBlockSizeOfInputText
from aes_encryption import encryptAES, decyrptAES

# Test function adaptBlockSizeOfInputText
testText = ''.join(random.choice(string.ascii_letters) for i in range(31))
resultText = testText + 'X'
outputText = adaptBlockSizeOfInputText(testText)
assert outputText == resultText

textToEncrypt = 'test'
key = '0123456789ABCDEF'
encryptedText = encryptAES(textToEncrypt, key)
print(type(encryptedText))
print(encryptedText)

textToDecrypt = encryptedText
decryptedText = decyrptAES(textToDecrypt, key)
print(decryptedText)
