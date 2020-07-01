def saludo(nombre, edad, domicilio="centro"):
    print(nombre)
    print(edad)
    print(domicilio)


saludo("oscar", "23", "altavista")


def conexion(ip, user, password, port=22):
    print(ip,user,password,port)

conexion("1.1.1.1", "oscar", "pepepe", "8181")