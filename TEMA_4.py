class Tarjeta:
    def __init__(self, numero, titular, banco, saldo=0.0, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.banco = banco
        self.saldo = saldo
        self.limite = limite

    def mostrar_datos(self):
        return (f"Número: {self.numero}\n"  
                f"Titular: {self.titular}\n"
                f"Banco: {self.banco}\n"
                f"Saldo: {self.saldo}\n"
                f"Límite: {self.limite}\n")
    