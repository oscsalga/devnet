import requests
import json

urlToken = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"
urlGet = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-7.json"
headers = {"Content-Type": "application/json"}
payload = '{"aaaUser":{"attributes": {"name": "admin","pwd": "ciscopsdt"}}}'

r = requests.post(urlToken, headers=headers, verify=False, data=payload)

rJson = r.json()
token = rJson["imdata"][0]["aaaLogin"]["attributes"]["token"]
print(token)
cookie = {}
cookie["APIC-Cookie"] = token
print(cookie)

r = requests.get(urlGet, headers=headers, verify=False, cookies=cookie).json()
print(r)