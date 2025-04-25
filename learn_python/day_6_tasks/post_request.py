import requests
import json

json_body = json.dumps({
  "postcodes" : ["b152et"]
})
headers = {'Content-Type': 'application/json'}

post_codes_req = requests.post('https://api.'
                               'postcodes.io/'
                               'postcodes',
                               headers=headers,
                               data=json_body)

print(post_codes_req)
print(post_codes_req.status_code)
print(post_codes_req.headers)
print(post_codes_req.content)
print(post_codes_req.json()['result'])
for pc in post_codes_req.json()['result']:
    print(pc['result']['postcode'], " | ",
          pc['result']['region'], " | ",
          pc['result']['ccg'])
