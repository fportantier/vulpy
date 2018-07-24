#!/usr/bin/env python3

import sys

from binascii import unhexlify

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

key = sys.argv[1].encode()
iv = unhexlify(sys.argv[2])
msg = unhexlify(sys.argv[3])

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(key)
key_digest = digest.finalize()

cipher = Cipher(algorithms.AES(key_digest), modes.CFB(iv), backend=default_backend())
decryptor = cipher.decryptor()
plain = decryptor.update(msg) + decryptor.finalize()

print(plain.decode(errors='ignore'))
