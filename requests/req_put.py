import json
import requests

info = {'name': 'Homa', 'id': '9223372036854771974'}
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
res = requests.put(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(info, ensure_ascii=False))

print(res.status_code)
print(res.json())
