from deportista import Deportista
from persona import Persona


class Futbolista(Persona, Deportista):
    
    _listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil) -> None:
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)

        self._golesMarcados:int = golesMarcados
        self._tarjetasRojas:int = tarjetasRojas
        self._piernaHabil:str = piernaHabil

        Futbolista._listaFutbolistas.append(self)

    def __str__(self) -> str:
        return f"Mi nombre es {self._nombre} soy profesional en el deporte {self._deporte} Tengo {self._edad} años de edad y llevo {self._añosPracticando} años en el deporte"

    def getGolesMarcados(self):
        return self._golesMarcados
        
    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil