#!/usr/bin/env python3

import sys
import os
from binascii import hexlify

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

password = sys.argv[1].encode()
backend = default_backend()
salt = os.urandom(16)

# derive
kdf = Scrypt(
    salt=salt,
    length=32,
    n=2**14,
    r=8,
    p=1,
    backend=backend
)

key = kdf.derive(password)

print(hexlify(salt).decode(), hexlify(key).decode())


'''
# verify
kdf = Scrypt(
salt=salt,
length=32,
n=2**14,
r=8,
p=1,
backend=backend
)
kdf.verify(b"my great password", key)
'''


