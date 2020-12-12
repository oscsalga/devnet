import Base as db
import random
import time
import os
import threading

ips = ["1.1.1.1", "172.18.87.85", "172.18.87.93", "172.18.87.79", "172.18.104.39", "172.18.104.34", "172.18.87.91",
      "172.18.120.160", "172.18.87.109", "172.18.120.141", "172.18.104.43"]

comando = "admin show env fan"


def fan(listaIP):
    listaIP2 =[]
    listaIP2.append(listaIP)
    for ip in listaIP2:
        print(ip)
        for i in range(2):
            try:
                esperar = random.randint(1, 2)
                #print("ESPERANDO: " + str(esperar))
                time.sleep(esperar)
                conexion = db.Drops(ip)
            except:
                continue  # retrying
            else:
                break
        else:
            continue

        hostname = conexion.findHostname()
        print(hostname)
        fans = conexion.ejecutarComando(comando)
        print(fans.split())

        if str("0") in fans.split():
            print("ZERO ON A FAN")
            conexion.correo(hostname, ['oscsalga@cisco.com'], fans)
        else:
            print("no hay cero")
            #conexion.correo(hostname, ['oscsalga@cisco.com'], fans)
        conexion.desconectar()

lista = []
for ip in ips:

    th = threading.Thread(target=fan, args=(ip,))
    lista.append(th)

for x in lista:
    x.start()
for x in lista:
    x.join()
#fan(ips)