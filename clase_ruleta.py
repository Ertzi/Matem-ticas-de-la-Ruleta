import random

class Ruleta():
    """
    Clase para simular la ruleta, con diferentes modos de juego:
    - 'color': apuestas todo a un color
    - 'par_impar': apuestas todo a que salga par o impar
    - 'pasa_falta': pasa = 1-18, falta = 19-36
    - 'docena': apuestas todo a que salga una docena de las tres que hay (1-12, 13-24, 25-36)
    - 'dos_docenas': lo mismo pero a dos de las tres docenas
    - 'columnas': se apuesta a una de las tres columnas que hay
    - 'dos_columnas': Se apuesta a dos de las tres columnas que hay
    - 'seisena': 
    - 'cuadro':
    - 'transversal': 
    - 'caballo': 
    - 'pleno': 
    """
    def __init__(self, modo_de_juego):
        self.modo_de_juego = modo_de_juego

        self.__negro = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.__rojo =  [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    def __conseguir_valor(self):
        return random.randint(0,36)
    
    def __apostar_color(self, cantidad, color): # __ para no poder acceder a la funcion desde fuera de la clase
        valor = self.__conseguir_valor()
        if valor in self.__negro and color == "negro":
            return cantidad * 2
        elif valor in self.__rojo and color == "rojo":
            return cantidad * 2
        else:
            return 0
    
    def __apostar_par_impar(self, cantidad, paridad):
        valor = self.__conseguir_valor()
        if valor != 0:
            if valor % 2 == 0 and paridad == "par":
                return cantidad * 2
            elif valor % 2 != 0 and paridad == "impar":
                return cantidad * 2
            else:
                return 0
        else:
            return 0
    
    def apostar(self, cantidad, color = "negro", paridad = "par"):
        if self.modo_de_juego == "color":
            return self.__apostar_color(cantidad, color)
        
        elif self.modo_de_juego == "par_impar":
            return self.__apostar_par_impar(cantidad, paridad)

        
