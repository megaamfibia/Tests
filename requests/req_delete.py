import json
import requests

info = {'id': '9223372036854771968'}
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
res = requests.delete(f'https://petstore.swagger.io/v2/pet/9223372036854771968', headers=headers,
                      data=json.dumps(info, ensure_ascii=False))

print(res.status_code)
print(res.json())