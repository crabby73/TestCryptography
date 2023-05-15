from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument("-f", "--file", dest="infile", default="none")
parser.add_argument("-o", "--operation", dest="operation", default="encode")
parser.add_argument("-k", "--key", dest="key", type=int, default=0)

args = parser.parse_args()

print(args.infile)
print(args.operation)
print(args.key)