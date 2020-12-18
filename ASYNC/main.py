#  CODED BY OSCAR SALGADO ORTIZ - OSCSALGA@CISCO.COM
#  pip3 install netdev bs4 colorama requests

import asyncio
import netdev
from datetime import datetime
import bs4
import requests
import sys
import colorama

url = "http://172.18.104.30/rtp_xr.html"
username = ""
password = ""
comandos = ["show plat"]


def obtainIps() -> list:
    r = requests.get(url)
    listaIps = []
    soup = bs4.BeautifulSoup(r.text, "html.parser")

    links_with_text = []
    for a in soup.find_all('a', href=True):
        if a.text:
            links_with_text.append(a['href'])

    for x in links_with_text:
        if "ssh" in x:
            listaIps.append(x[6:])
    return listaIps


def leerIps() -> list:
    with open("listaIps2", "r") as f:
        ips = f.read().splitlines()
        return ips


async def conectar(ip: dict, comandos: list) -> None:
    try:
        async with netdev.create(**ip) as ios:
            for command in comandos:
                output = await ios.send_command(command)
                hostname = ios.base_prompt
                print(colorama.Fore.BLUE + hostname)
                if "Invalid input detected at" not in output:
                    saveLog("OUTPUT", ip["host"], f"Hostname: {hostname}\n{output}")
                else:
                    print(output)
            await ios.disconnect()

    except Exception as e:
        saveLog("ERROR", ip["host"], str(e))
        #print(str(e))


def saveLog(archivo, ip, texto, hostname="") -> None:
    with open(archivo, "a") as f:
        f.write(f"IP: {ip}  {hostname}\n{texto}\n" + "*" * 80 + "\n")


def llenar() -> list:
    devices = []
    if username == "" or password == "" or (username == "" and password == ""):
        print(colorama.Fore.RED + "\033[1m" + "Username y/o Password en blanco" + "\033[0m")
        sys.exit()
    for ip in obtainIps():
        dev = {'username': username,
               'password': password,
               'device_type': 'cisco_ios_xr',
               'host': ip,
               'port': 22
               }
        devices.append(dev)
    return devices


async def show_commands() -> None:
    if not comandos:
        print(colorama.Fore.RED + f"Comandos Empty")
        sys.exit()
    devices = llenar()
    #comandos = ["show ver", "show ipv4 int br", "show plat", "show run"]
    print(colorama.Fore.YELLOW + "\033" + "*" * 50)
    print(colorama.Fore.YELLOW + "\033[1m" + f"    **** Lista de Comando: {comandos} ****")
    print(colorama.Fore.YELLOW + "\033" + "*" * 50)
    tasks = [conectar(dev, comandos) for dev in devices]
    await asyncio.wait(tasks)


def main() -> None:

    start_time = datetime.now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(show_commands())
    exec_time = (datetime.now() - start_time).total_seconds()
    print(colorama.Fore.LIGHTGREEN_EX + "\033[1m" + f"***********Summary: it took {exec_time:,.2f} "
                                                    f"seconds to Finish***********")


if __name__ == '__main__':
    colorama.init()
    main()
