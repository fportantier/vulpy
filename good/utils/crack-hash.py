#!/usr/bin/env python3

import hashlib
import sys

candidate = sys.argv[1]

for number in range(10000):
    h = hashlib.sha512(str(number).encode()).hexdigest()
    if h == candidate:
        print('Cracked! Password:', number)

