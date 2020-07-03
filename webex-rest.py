# curl -X GET "https://webexapis.com/v1/rooms"
# -H "Authorization: Bearer NmJjZGVjZmMtZWEyMC00NThmLWJjNGMtMGNkZTU4N2Y1NWU1MGFhYWYxYzgtZWM5_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
# -H "Accept: application/json"

import requests
import json

url = "https://webexapis.com/v1/rooms"
token = "Bearer NmJjZGVjZmMtZWEyMC00NThmLWJjNGMtMGNkZTU4N2Y1NWU1MGFhYWYxYzgtZWM5_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
headers = {"Accept": "application/json",
           "Authorization": token}

r = requests.get(url, headers=headers)

print(json.dumps(r.json(), indent=2))