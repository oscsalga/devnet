# sudo pip3 install ucsmsdk
from ucsmsdk.ucshandle import UcsHandle

url = "10.10.20.113"
username = "ucspe"
password = "ucspe"

conn = UcsHandle(url, username, password)
conn.login()  # iniciar conexion

org = conn.query_classid("computeBlade")

for x in org:
    print(x)  # podemos acceder a cada uno de ellos por ejemplo: x.dn, x.number_of_cpus, etc

blade = conn.query_dn("sys/chassis-6/blade-8")
print(blade)

conn.logout()  # desconectar
