import json
import base64

s = base64.b64encode(json.dumps({'username': 'fabian'}).encode())

print(s)

