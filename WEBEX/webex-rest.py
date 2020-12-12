# curl -X GET "https://webexapis.com/v1/rooms"
# -H "Authorization: Bearer "
# -H "Accept: application/json"

import requests
import json

url = "https://webexapis.com/v1/rooms"
clave = "ZWZkNjIyMmQtZWRkYS00N2IwLWJhMTMtODQyMWIzM2E4Y2FhYzBhYWIyMTYtNmY2_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
token = f"Bearer {clave}"
headers = {"Accept": "application/json",
           "Authorization": token}

roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vOGQxODVlYzAtZTBkMi0xMWVhLTk4MjUtM2I3Zjk4MThjODYz"

r = requests.get(url, headers=headers).json()
requests.post(url, headers=headers)

# print(r.status_code) # IMPRIME 200 SI ESTÁ BIEN
#p rint(r.ok) # IMPRIME True SI ESTÁ BIEN

for x in range(0, len(r["items"])):
    print(r["items"][x]["title"])


# curl -X GET "https://webexapis.com/v1/rooms" -H "Authorization: Bearer ODAzNGZlMjUtN2YxNC00MTE4LTkxYmUtYjZhYWMwMjY1NzU3Y2Y5OTg2ODQtMmRj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f" -H "Accept: application/json"
