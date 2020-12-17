from netmiko import ConnectHandler
from genericos import Genericos
import time


class Conexion:

    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.timeout = 20

    def conectar(self):
        try:
            tunnel = ConnectHandler(device_type="cisco_xr", ip=self.ip, password=self.password,
                                    port=self.port, username=self.username, timeout=self.timeout)
            if tunnel.is_alive() == True:
                return tunnel
            else:
                pass
        except Exception as e:
            fecha = time.strftime("%d/%m/%Y - %H:%M:%S")
            Genericos.save_to_file("ERROR", fecha + " " + self.ip, str(e))
            print(str(e))






