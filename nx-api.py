import requests
import json

url = "https://sbx-nxos-mgmt.cisco.com/ins" # /ins OBLIGATORIO
user = "admin"
password = "Admin_1234!"

# "Content-type": "application/json" para configurar + cli_conf
# para show "Content-type": "application/json-rpc" + cli_show

headers = {"Content-type": "application/json"}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show runn",
    "output_format": "json"
  }
}

r = requests.post(url, data=json.dumps(payload), headers=headers, verify=False, auth=(user, password))

print(json.dumps(r.json(), indent=2, sort_keys=True))
