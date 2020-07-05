# sudo pip3 install webexteamssdk
from webexteamssdk import WebexTeamsAPI

token = "OTRjMzA1YTgtMjg5NC00NzU5LThlNmItNTFmZWM5MmVjZjRkMjYxNjIyNWQtYzZk_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
constructor = WebexTeamsAPI(access_token=token)


for x in constructor.rooms.list():
    print(x.title)
    print(x.)

