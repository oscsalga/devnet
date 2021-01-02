import requests
import os
import json
import threading
from os import path
import enquiries

accept = "application/json, text/plain, */*"
x_requested_with = "com.my.ine"
sec_fetch_site = "cross-site"
sec_fetch_mode = "cors"
sec_fetch_dest = "empty"
content_type = "application/json;charset=UTF-8"
accept_encodings = "gzip, deflate, br"
login_url = "https://uaa.ine.com/uaa/authenticate"
token_path = "token.txt"
auth_check_url = "https://uaa.ine.com/uaa/auth/state/status"


def course_list(page):
    url = "https://content-api.rmotr.com/api/v1/courses"


    try:
        r = requests.get(f"{url}?page={page}")
        for y in range(len(r.json()["results"])):

            with open("FullList", "a") as f:
                f.write("Title: " + r.json()["results"][y]["name"] + "\n")
                f.write("URL: " + r.json()["results"][y]["url"] + "\n")
                f.write("CourseID: " + r.json()["results"][y]["id"] + "\n")
                f.write("*" * 100)
                f.write("\n")
    except:
        pass


def get_courses():
    print("Please wait, not too much")
    lista = []
    url = "https://content-api.rmotr.com/api/v1/courses"

    r = requests.get(url)
    count = r.json()["count"]

    for x in range(1, count + 1):
        th = threading.Thread(target=course_list, args=(x,))
        lista.append(th)

    for x in lista:
        x.start()
    for x in lista:
        x.join()


def login():
    global access_token
    global refresh_token
    host = "uaa.ine.com"
    header = {"Host": host, "Accept": accept,"X-Requested-With": x_requested_with,"Accept-Encoding": accept_encodings,"sec-fetch-mode": sec_fetch_mode,"sec-fetch-dest": sec_fetch_dest,"Content-Type": content_type}
    user_name = ""
    #password = getpass.getpass(prompt="Enter your Password: \n")
    password = ""
    login_data = {"username": user_name,"password": password}
    login_data = json.dumps(login_data)
    login_data = requests.post(login_url,headers = header,data = login_data)
    if login_data.status_code == 200:
        login_data = json.loads(login_data.text)
        access_token = login_data["data"]["tokens"]["data"]["Bearer"]
        refresh_token = login_data["data"]["tokens"]["data"]["Refresh"]
        with open(token_path,'w') as fp:
            tokens = {"access_token": access_token,"refresh_token": refresh_token}
            fp.write(json.dumps(tokens))
            access_token = "Bearer " + access_token
        auth_check()
        #print(access_token)
        return access_token
    elif(login_data.status_code == 403):
        print("Username or password is incorrect\n ")
        exit()
        

def auth_check():
    host = "uaa.ine.com"
    header = {"Authorization": access_token, "Accept": accept,"X-Requested-With": x_requested_with,"Accept-Encoding": accept_encodings,"sec-fetch-mode": sec_fetch_mode,"sec-fetch-dest": sec_fetch_dest,"Content-Type": content_type}
    auth_valid = requests.get(auth_check_url, headers=header)
    user = json.loads(auth_valid.text)
    if auth_valid.status_code == 200:
        if user["data"]["email"]:
            email = user["data"]["email"]
            fname = user["data"]["profile"]["data"]["first_name"]
            lname = user["data"]["profile"]["data"]["last_name"]
            print("Logged in to INE as {} {} with {}\n".format(fname, lname, email))


def main(courseId):
    if path.exists(token_path):
        f = open(token_path, "r")
        bearer = f.read()
        headers = {"Authorization": "Bearer " + json.loads(bearer)["access_token"]}
    else:
        bearer = login()
        headers = {"Authorization": bearer}
        #print(bearer)
    s = requests.get("https://video.rmotr.com/api/v1/videos/5703efb6-011f-4818-818f-844ef16242a0/media", headers=headers)
    #print(s.status_code)

    if s.status_code != 200:
        bearer = login()
        headers = {"Authorization": bearer}

    url = f"https://content-api.rmotr.com/api/v1/courses?ids={courseId}"

    r = requests.get(url)
    nombreCurso = r.json()["results"][0]["name"]
    print(nombreCurso)
    
    cont1 = 1
    for x in range(0, len(r.json()["results"][0]["content"])):
        folder = r.json()["results"][0]["content"][x]["name"]
        for y in r.json()["results"][0]["content"][x]["content"]:
            cont2 = 1
            for z in y["content"]:
                titulo = y["name"].replace("/", "").replace(".", "")
                r2 = requests.get(f"https://video.rmotr.com/api/v1/videos/{z['uuid']}/media".strip(), headers=headers)
                if "detail" in json.loads(json.dumps(r2.json())):
                    continue
                urlVideo = json.dumps(r2.json()["playlist"][0]["sources"][3]["file"])
                os.system((f"youtube-dl {urlVideo} --hls-prefer-native -o "
                           f"'{nombreCurso}/{cont1}-{titulo}/{cont2}-{r2.json()['title']}.mp4'"))
                cont2 += 1
            cont1 += 1


def start():
    options = ['Get Full List', 'Download', "Exit"]
    choice = enquiries.choose('Choose one of these options: ', options)

    if choice == "Get Full List":
        get_courses()
        print("Full List downloaded to 'FullList File'")
        start()

    elif choice == "Download":
        #  EXAMPLE: a4a4785c-4271-11e4-a79f-22000b3582a3
        courseId = input("ENTER THE COURSEID: ").strip()
        main(courseId)

    elif choice == "Exit":
        exit()
start()