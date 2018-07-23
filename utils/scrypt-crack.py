#!/usr/bin/env python3

import sys
import os
import binascii
from binascii import unhexlify

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey

try:
    salt = unhexlify(sys.argv[1].encode())
    key = unhexlify(sys.argv[2].encode())
except binascii.Error:
    print('Non-hexadecimal data on salt and/or key', file=sys.stderr)
    sys.exit(1)

backend = default_backend()


for number in range(10000):

    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=backend
    )

    try:
        kdf.verify(str(number).encode(), key)
        print('Cracked! Password:', number)
        break
    except InvalidKey:
        pass

