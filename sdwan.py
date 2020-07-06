import requests
import urllib3
import sys
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://sandboxsdwan.cisco.com:8443/j_security_check"
urlDevice = "https://sandboxsdwan.cisco.com:8443/dataservice/device"

payload = {'j_username': 'devnetuser',
          'j_password': 'Cisco123!'}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'JSESSIONID=xUn_yujV7VuVhQsmpV0lEKJI_UNP5nnLIb_CmRA5.4854266f-a8ad-4068-9651-d4e834384f51'
}

sesion = requests.session() # to obtain a COOKIE
response = sesion.post(url, data=payload, verify=False)

# SESSION WILL """"ALWAYS"""" SHOW 200 OK STATUS CODE
# BUT IF THE LOGIN IS NOT CORRECT IT WILL SHOW SOME TEXT
# IF THE LOGIN IS 100% CORRECT IT WILL SHOW 200 OK RESPONSE AND NO TEXT

if response.status_code == 200 and not response.text:
    #print("Login Correct, statuscode = 200 and no text")
    pass
else:
    print("Wronggggggg")
    sys.exit()

r = sesion.get(urlDevice, verify=False)
#print(json.dumps(r.json()["data"], indent=2))

for device in r.json()["data"]:
    print(f"Hostname: {device['host-name']}")
    print(f"Local IP: {device['local-system-ip']}")
    print(f"Model: {device['device-model']}")
    print("*" * 30)
