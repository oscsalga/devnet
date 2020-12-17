from conexion import Conexion
from ejecutar import Ejecutar
import threading
from genericos import Genericos


class Main:

    @staticmethod
    def run(ip):
        conn = Conexion(ip, "oscsalga", "Ximena8.")
        tunnel = conn.conectar()
        if tunnel == None:
            pass
        else:
            com = Ejecutar(tunnel)
            try:
                hostname = com.hostname()
                texto = com.ejecutar_comando(["show ver"])
                #texto = com.ejecutar_comando("show ver")
                Genericos.save_to_file("output", hostname, "")
                print(texto)
            except:
                pass
            finally:
                com.desconectar()

def leerIps():
    with open("listaIps", "r") as f:
        ips = f.read().splitlines()
        return ips

lista = []

for ip in leerIps():
    th = threading.Thread(target=Main.run, args=(ip,))
    lista.append(th)

for x in lista:
    x.start()
for x in lista:
    x.join()



