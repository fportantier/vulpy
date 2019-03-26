#!/usr/bin/env python3

from binascii import hexlify

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA512(), backend=default_backend())

with open('/bin/ls', 'rb') as f:
    data = f.read()

digest.update(data)
hexdigest = hexlify(digest.finalize()).decode()

print('{:<12} {}'.format('sha512', hexdigest))

