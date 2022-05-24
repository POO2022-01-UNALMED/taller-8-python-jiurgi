class Persona:

    def __init__(self, nombre, edad, altura, sexo) -> None:
        self._nombre: str = nombre
        self._edad: int = edad
        self._altura: str = altura
        self._sexo: str = sexo

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getAltura(self):
        return self._altura

    def getSexo(self):
        return self._sexo

    def setNombre(self, Nombre):
        self._nombre = Nombre

    def setEdad(self, Edad):
        self._edad = Edad

    def setAltura(self, Altura):
        self._altura = Altura

    def setSexo(self, Sexo):
        self._sexo = Sexo

        