# sudo pip3 install webexteamssdk
from webexteamssdk import WebexTeamsAPI
import time

token = ""
constructor = WebexTeamsAPI(access_token=token)



#for x in constructor.rooms.list():
#    print(x.title)
#    print(x.id)
#    print("*" * 100)
#    print(x)


for x in constructor.messages.list("Y2lzY29zcGFyazovL3VzL1JPT00vYTM4Mjc3NjAtYWFkMi0xMWU3LWFlZTMtNjM1MTRmN2FlODgy"):
    print(x.text)
