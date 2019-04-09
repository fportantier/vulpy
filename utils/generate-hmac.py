#!/usr/bin/env python3

import sys

from binascii import hexlify

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac

key = sys.argv[1].encode()
msg = sys.argv[2].encode()

h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
h.update(msg)

print(hexlify(h.finalize()).decode())

