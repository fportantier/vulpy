
import sys
import hashlib, binascii
import time
import os

#os.urandom(n)

result = []

ROUNDS=100
MULTI=float(1000000 / ROUNDS)

t1 = time.process_time()
a1 = time.time()
for n in range(ROUNDS):
    dk = hashlib.pbkdf2_hmac('sha256', sys.argv[1].encode(), os.urandom(16), 100000)
result.append(('pbkdf2', (time.time() - a1) * MULTI))



for algo in hashlib.algorithms_available:
    a1 = time.time()
    for n in range(ROUNDS):
        h = hashlib.new(algo)
        h.update(sys.argv[1].encode())
        #print(time.process_time() - t1, algo)

    #print((time.time() - a1) * MULTI, algo)
    result.append((algo, (time.time() - a1) * MULTI))
#from pprint import pprint
for r in sorted(result, key=lambda r: r[1], reverse=True):
    print('{:.4f} - {}'.format(r[1], r[0].upper()))
