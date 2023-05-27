import string

def readInputFile(file) -> string:
    lines = list()

    try:
        f = open(file, 'r')
    except OSError:
        print('cannot open', file)
        exit(1)
    else:
        lines = f.readlines()
        f.close()

    return lines


def writeOutputFile(text):
    try:
        f = open("output.txt", "x")
    except OSError:
        print('File already exists: ', "output.txt")
        exit(1)
    else:
        for line in text:
            f.writelines(line + "\n")
        f.close()


def readFileInOneBlock(text) -> string:
    try:
        f = open(file, 'r')
    except OSError:
        print('cannot open', file)
        exit(1)
    else:
        text = f.read()
        f.close()

    return text


def writeFileInOneBlock(text):
    try:
        f = open("output.txt", "x")
    except OSError:
        print('File already exists: ', "output.txt")
        exit(1)
    else:
        f.write(text)
        f.close()
