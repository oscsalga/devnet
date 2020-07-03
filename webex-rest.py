# curl -X GET "https://webexapis.com/v1/rooms"
# -H "Authorization: Bearer NmJjZGVjZmMtZWEyMC00NThmLWJjNGMtMGNkZTU4N2Y1NWU1MGFhYWYxYzgtZWM5_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
# -H "Accept: application/json"

import requests
import json

url = "https://webexapis.com/v1/rooms"
token = "Bearer NmJjZGVjZmMtZWEyMC00NThmLWJjNGMtMGNkZTU4N2Y1NWU1MGFhYWYxYzgtZWM5_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
headers = {"Accept": "application/json",
           "Authorization": token}

r = requests.get(url, headers=headers).json()

# print(r.status_code) # IMPRIME 200 SI ESTÁ BIEN
#p rint(r.ok) # IMPRIME True SI ESTÁ BIEN

for x in range(0, len(r["items"])):
    if "Francisco" in r["items"][x]["title"]:
        id = r["items"][x]["id"]
        print("https://webexapis.com/v1/messages?roomId=" + id)
        mensaje = requests.get("https://webexapis.com/v1/messages?roomId=" + id, headers=headers).json()

        for y in range(len(mensaje["items"]) * -1, 1):
            try:
                print(f"Mensaje Numero: {y}")
                print(mensaje["items"][y]["text"])
                print("*" * 100)
            except:
                pass
