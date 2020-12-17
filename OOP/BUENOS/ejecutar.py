from genericos import Genericos

class Ejecutar:

    def __init__(self, conexion):
        self.conexion = conexion

    def ejecutar_comando(self, comando):
        lista = []
        output = ""
        for c in comando:
            print(c)
            try:
                output = output + self.conexion.send_command(c, delay_factor=2)
            except Exception as e:
                Genericos.save_to_file("ERROR_EJECUTAR", self.hostname(), str(e))

        return output

    def ejecutar_comando_config(self, comando):
        output = self.conexion.send_config_set(comando)
        return output

    def hostname(self):
        try:
            host = self.conexion.find_prompt()
            return host
        except:
            pass

    def desconectar(self):
        self.conexion.cleanup()
        self.conexion.disconnect()

