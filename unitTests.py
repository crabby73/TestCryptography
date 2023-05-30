import random
import string
from aes_encryption import adaptBlockSizeOfInputText

# Test function adaptBlockSizeOfInputText
testText = ''.join(random.choice(string.ascii_letters) for i in range(31))
resultText = testText + 'X'
outputText = adaptBlockSizeOfInputText(testText)
assert outputText == resultText


