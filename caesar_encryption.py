import string


def createAlphabet():
    letters = list(string.ascii_letters)
    return letters[26:]


def createEncryptionTable(key):
    alphabet = createAlphabet()
    encryption = list()
    i = key % 26
    count = 0
    while count < 26:
        encryption.append(alphabet[i])
        i = i + 1
        if i > 25:
            i = 0
        count = count + 1

    return dict(zip(alphabet,encryption))


def encryptText(text, key):
    encryptionTable = createEncryptionTable(key)
    upperText = text.upper()
    encryptedText = list()
    alphabet = createAlphabet()
    for letter in upperText:
        if letter in alphabet:
            encryptedText.append(encryptionTable[letter])

    output = ""
    return output.join(encryptedText)


def decryptText(text, key):
    upperText = text.upper()
    encryptionTable = createEncryptionTable(key)
    decryptionTable = {y: x for x, y in encryptionTable.items()}
    decryptedText = list()
    alphabet = createAlphabet()
    for letter in upperText:
        if letter in alphabet:
            decryptedText.append(decryptionTable[letter])

    output = ""
    return output.join(decryptedText)



