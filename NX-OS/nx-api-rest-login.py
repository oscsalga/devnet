import requests
import json

username = "admin"
password = "Admin_1234!"
urlLogin = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"
urlGet = "https://sbx-nxos-mgmt.cisco.com//api/node/mo/sys/bd/bd-[vlan-10].json"

headers = {"Content-Type": "application/json"}
payload = '{"aaaUser":{"attributes": {"name": "admin","pwd": "Admin_1234!"}}}'

r = requests.post(urlLogin, headers=headers, verify=False, data=payload)

rJson = r.json()
token = rJson["imdata"][0]["aaaLogin"]["attributes"]["token"]
# NO PODEMOS USAR TOKEN DIRECTAMENTE
# NECESITAMOS CREAR UN HEADER COOKIE
# print(token)

print(headers)

cookie = {}
cookie["APIC-Cookie"] = token
print(headers)

r = requests.get(urlGet,headers=headers, verify=False, cookies=cookie)
# IMPRIMIR LA SALIDA EN FORMATO JSON INDENTADO
print(json.dumps(r.json(), indent=2, sort_keys=True))