import requests
import json
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = "oscsalga"
password = "UGkfrDxb"
urlToken = "https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/auth/generatetoken"
urlDevices = "https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/devicegroups/devicegrouprecords"
urlObjectsMonitoring = "https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/applications"
headers = {"Content-type": "application/json"}

r = requests.post(urlToken, headers=headers, auth=(username, password), verify=False)

if r.status_code == 204:  # STATUS CODE FOR OK BUT WITH NO CONTENT
    token = r.headers["X-auth-access-token"]
else:
    print("Code 401")  # CODE 401 ERROR ON TOKEN
    sys.exit()
print(r.headers)  # Nos muestra X-auth-access-token dentro del diccionario

print(token)
headers['X-auth-access-token'] = token

r = requests.get(urlDevices, headers=headers, verify=False)

print(r.json()["links"])
for x in r.json()["items"]:
    print(x["name"])

r = requests.get(urlObjectsMonitoring, headers=headers, verify=False)
#print(r.json()["items"])

for apps in r.json()["items"]:
    print(f"Apps Monitoring: {apps['name']}")

