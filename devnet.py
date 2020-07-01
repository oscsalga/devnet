from netmiko import ConnectHandler
import datetime
import time
import re
import subprocess
import smtplib
import os
import sys
import re


hostname = "sbx-iosxr-mgmt.cisco.com"
user = "admin"
password = "C1sco12345"
port = 8181
timeout = 20


tunnel = None

inicio = 0
final = 0
incremento = 0


def conexion():
    try:
        net_connect = ConnectHandler(device_type='cisco_xr', ip=hostname, port=port,
                                              username=user, password=password, timeout=timeout)
        return net_connect
    except Exception as e:
        print("el error fue: " + str(e))
        sys.exit()


def mandarComando(comando):
    try:
        output = tunnel.send_command(comando)
        print(output)
        return output
    except Exception as e:
        print("el error fue: " + str(e))
        sys.exit()

def desconectar():
    tunnel.disconnect()

def guardarTexto(archivo, modo, texto):
    with open(archivo, modo) as archivo:
        archivo.write(texto + "\n")

tunnel = conexion()
salida = mandarComando("show ip int brief")
salida = salida.split()


inicio = salida.index("Vrf-Name") + 1
final = len(salida)
incremento = salida[inicio:]
incremento = incremento.index("default") + 1
#print(incremento)

for inter in range(inicio, final, incremento):
    guardarTexto("output.log", "a", mandarComando("show interface " + salida[inter]))

desconectar()


