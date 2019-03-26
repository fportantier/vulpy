#!/usr/bin/env python3

import nacl.encoding
import nacl.hash

with open('/bin/ls', 'rb') as f:
    data = f.read()

HASHER = nacl.hash.sha512

digest = HASHER(data, encoder=nacl.encoding.HexEncoder).decode()

print('{:<12} {}'.format('sha512', digest))

