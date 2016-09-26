import sys
import argparse
import hashlib

algos = [ a.lower() for a in hashlib.algorithms_available ]
algos_help = "Any of: " + ', '.join(algos)

parser = argparse.ArgumentParser(description='Generate hashes')
parser.add_argument('algorithm', help=algos_help)
parser.add_argument('text', help='text to hash')

args = parser.parse_args()

if args.algorithm not in algos:
    parser.print_help()
    sys.exit(1)

h = hashlib.new(args.algorithm)
h.update(args.text.encode())
print(h.hexdigest())

