import requests
import os
import json

"""
API INE
{
    "courses": "http://content-api.rmotr.com/api/v1/courses",
    "vendors": "http://content-api.rmotr.com/api/v1/vendors",
    "categories": "http://content-api.rmotr.com/api/v1/categories",
    "learning-areas": "http://content-api.rmotr.com/api/v1/learning-areas",
    "tags": "http://content-api.rmotr.com/api/v1/tags",
    "instructors": "http://content-api.rmotr.com/api/v1/instructors",
    "passes": "http://content-api.rmotr.com/api/v1/passes",
    "user-access": "http://content-api.rmotr.com/api/v1/user-access",
    "learning-paths": "http://content-api.rmotr.com/api/v1/learning-paths",
    "content-issues": "http://content-api.rmotr.com/api/v1/content-issues"
}
"""

course = "9843c828"
url = f"https://content-api.rmotr.com/api/v1/courses?ids={course}"

r = requests.get(url)
nombreCurso = r.json()["results"][0]["name"]
print(nombreCurso)
headers = {"Authorization": "Bearer "
"eyJraWQiOiJsNlRId2RYZXdRTmh5NlJ2QTB2YnZnT0NPeWVaUkxvazM2b205dnU1Q0hFPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiZmUyYzE0OS1iZGUwLTQ2NTEtYmZjZC02ZDkxYTE1OWQwYjUiLCJldmVudF9pZCI6IjAzMDFkODk3LTdjYjgtNGZkYi04MjIwLWViYWI4OWJkYWQwNyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2MDYxNjY1MTgsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX2d4SWlFV2Z0QSIsImV4cCI6MTYwNjE3NDE1OCwiaWF0IjoxNjA2MTcwNTU4LCJqdGkiOiI3M2E0MDA2Ny02NTcxLTRkYTAtYjIwMy0xOTY3ZGYzMDlkNzEiLCJjbGllbnRfaWQiOiIyNHZxdWdmNzFlbW9kdjI5cDVzOXY2am9oOSIsInVzZXJuYW1lIjoiYmZlMmMxNDktYmRlMC00NjUxLWJmY2QtNmQ5MWExNTlkMGI1In0.j6SpmmS3_xRcUbyUZlrPMzHCMD0MtCV8pIYrxTIRTfyy6delUG_GwFSOKIW9bU31WgXsvcxRb5ewSkh5qR2CczMbsVO8RHvBV0oIiweYspQfAzxiyGxvESuwm6Yv2diz7Urm0itmoZcnrQV7bILfjtVkCXCSPJXuBOXUVrjiolKxwtmKZXfXYn20-6tERbgaTME4aSHQbSCVFL6HEqf-BMsnfy8gBodH-lQauDccXKxDsebD1BtAyD4JTXdwUpjkVGs6hZx0oJUK-2R-626e57HN-Vx7ce_uLsNqulwu3tepnA-0IHH9n9fFs9OvgCkICI_ekakGTvyggH44mTw-Lw"}
cont1 = 1
cont3 = 1
for x in range(0, len(r.json()["results"][0]["content"])):

    #print(r.json()["results"][0]["content"][x]["content"])

    folder = r.json()["results"][0]["content"][x]["name"]

    #print(r.json()["results"][0]["content"][x]["name"])  # TITULO

    for y in r.json()["results"][0]["content"][x]["content"]:
        #print(y["content"])
        #print(y["name"])
        #print(y)
        #print(r.json()["results"][0]["content"][x]["name"])
        cont2 = 1

        for z in y["content"]:
            #print(y["name"])  # FOLDER
            titulo = y["name"]
            #print(z["uuid"])
            #print(f"https://video.rmotr.com/api/v1/videos/{z['uuid']}/media".strip())
            r2 = requests.get(f"https://video.rmotr.com/api/v1/videos/{z['uuid']}/media".strip(), headers=headers)

            #print(r2.json())
            #print(json.dumps(r2.json(), indent=2))

            if "detail" in json.loads(json.dumps(r2.json())):
                continue
            #print(json.dumps(r2.json()["playlist"][0]["sources"][3]["file"]))
            #print(json.dumps(r2.json()["playlist"], indent=2))

            urlVideo = json.dumps(r2.json()["playlist"][0]["sources"][3]["file"])
            #print(titulo, folder, r2.json()["title"], urlVideo)
            os.system((f"youtube-dl {urlVideo} --hls-prefer-native -o '{nombreCurso}/{cont1}-{titulo}/{cont2}-{r2.json()['title']}.mp4'"))


            cont2 += 1
        cont1 += 1
