import requests
import json

url = "https://sbx-nxos-mgmt.cisco.com/ins"
user = "admin"
password = "Admin_1234!"
headers = {"Content-type": "application/json-rpc"}
payload = [
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show ip int br",
      "version": 1
    },
    "id": 1
  }
]

r = requests.post(url, data=json.dumps(payload), headers=headers, verify=False, auth=(user, password))

print(r.json())