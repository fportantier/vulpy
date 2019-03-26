#!/usr/bin/env python3

import hashlib

with open('/bin/ls', 'rb') as f:
    data = f.read()

h = hashlib.sha512(data).hexdigest()
print('{:<12} {}'.format('sha512', h))

