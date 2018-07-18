import hashlib
from time import time
# {'sha3_384', 'sha3_224', 'sha3_512', 'sha3_256', 'sha1', 'sha256', 'shake_128', 'sha224', 'shake_256', 'blake2b', 'md5', 'sha384', 'blake2s', 'sha512'}

values = list(range(10000, 59999))

algorithms = [
    'sha1',
    'sha256',
    'sha3_512',
]

for algo in algorithms:
    start = time()
    for value in values:
        h = hashlib.new(algo)
        h.update(bytes(value))
    print('{:>10} {}'.format(algo, time() - start))

#print(hashlib.algorithms_guaranteed)
#print(hashlib.algorithms_available)
#print(time())
