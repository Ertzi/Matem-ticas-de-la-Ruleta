import random

class Ruleta():
    """
    Clase para simular la ruleta, con diferentes modos de juego:
    - 'color': apuestas todo a un color
    """
    def __init__(self):
        self.__negro = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.__rojo =  [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    def __conseguir_valor(self):
        return random.randint(0,36)
    
    def apostar(self, cantidad, color = "negro"): # __ para no poder acceder a la funcion desde fuera de la clase
        valor = self.__conseguir_valor()
        if valor in self.__negro and color == "negro":
            return cantidad * 2
        elif valor in self.__rojo and color == "rojo":
            return cantidad * 2
        else:
            return 0


        
