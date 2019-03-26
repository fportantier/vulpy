#!/usr/bin/env python3

from Crypto.Hash import SHA512

with open('/bin/ls', 'rb') as f:
    data = f.read()

h = SHA512.new()
h.update(data)

print('{:<12} {}'.format('sha512', h.hexdigest()))

