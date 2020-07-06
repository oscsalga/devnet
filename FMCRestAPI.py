import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = "oscsalga"
password = "Fht2gvae"
urlToken = "https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/auth/generatetoken"
urlDevices = "https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/devicegroups/devicegrouprecords"
headers = {"Content-type": "application/json"}

r = requests.post(urlToken, headers=headers, auth=(username, password), verify=False)
print(r.headers["X-auth-access-token"])
token = r.headers["X-auth-access-token"]

headers['X-auth-access-token'] = token

r2 = requests.get(urlDevices, headers=headers, verify=False)

print(r2.json()["links"])
for x in r2.json()["items"]:
    print(x["name"])
