import platform


class Genericos:

    @classmethod
    def save_to_file(cls, archivo, hostname, texto):
        with open(archivo, "a") as f:
            f.write(str(hostname + "\n" + texto + "\n\n"))
            f.write("*" * 50)
            f.write("\n")
