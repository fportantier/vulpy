import sys
import hashlib

algorithm = sys.argv[1]
h = sys.argv[2]

for number in range(0, 1000):
    cvv = "{:03}".format(number).encode()
    result = hashlib.new(algorithm, cvv).hexdigest()
    if h == result:
        print('Cracked! CVV:', cvv.decode())
        break

