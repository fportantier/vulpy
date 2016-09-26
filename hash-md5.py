
import sys
import hashlib, binascii
import time
import os

h = hashlib.new('md5')
h.update(sys.argv[1].encode())
print(h.hexdigest())
