import random

class Ruleta():
    """
    Clase para simular la ruleta, con diferentes modos de juego:
    - Color: Apuestas todo a un color
    - Par / impar: apuestas todo a que salga par o impar
    - Docena: apuestas todo a que salga una docena de las tres que hay (1-12, 13-24, 25-36)
    - Personalizado: apuestas una(s) cantidad(es) en alguna(s) casilla(s)
    """
    def __init__(self, modo_de_juego):
        self.modo_de_juego = modo_de_juego

        self.negro = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.rojo =  [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    def apostar(self):
        pass