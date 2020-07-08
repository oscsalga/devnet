import requests
import json
import urllib3

# DISABLE SSL WARNING
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = "developer"
password = "C1sco12345"
urlBase = "https://ios-xe-mgmt-latest.cisco.com"
port = 9443
url = f"{urlBase}:{port}/restconf/data/native"


## HEADER PUEDE QUEDAR COMO AUTHORIZATION BASIC Y USER Y PASS COMO BASE64
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json",
           "Authorization": "Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU="}

'''headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json",
           "Authorization": "Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU="}'''


r = requests.get(url, headers=headers, verify=False)
## REQUEST PUEDE CONTENER EL PARAMETRO AUTH= O BASIC EN EL HEADER
##r = requests.get(url, auth=(username, password), headers=headers, verify=False)

rJson = r.json()

print(json.dumps(rJson, indent=2))