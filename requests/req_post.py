import json
import requests

info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Bubuska",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
res = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(info, ensure_ascii=False))

print(res.status_code)
print(res.json)
print(res.content)