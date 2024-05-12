import numpy as np
import matplotlib.pyplot as plt
import random
import os

directorio_actual = os.path.dirname(os.path.realpath(__file__))

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

ruleta = Ruleta()


def hay_dinero_suficiento(dinero,apuesta):
    return dinero >= apuesta

def simulacion_turno(turnos, dinero_inicial, dinero_minimo_apuesta):
    se_ha_perdido = False
    historial_dinero = np.zeros(turnos)
    historial_apuesta = np.zeros(turnos)
    dinero = dinero_inicial # Dinero al inicio 
    historial_dinero[0] = dinero

    # Apostar:
    apuesta = dinero_minimo_apuesta
    dinero -= apuesta
    historial_apuesta[0] = apuesta

    for i in range(1, turnos):
        historial_apuesta[i] = apuesta
        ganancias = ruleta.apostar(apuesta)
        if ganancias == 0 and hay_dinero_suficiento(dinero, apuesta * 2): 
            apuesta = apuesta * 2
            dinero -= apuesta
        elif ganancias == 0 and not hay_dinero_suficiento(dinero, apuesta * 2):
            historial_dinero[i:] = dinero
            se_ha_perdido = True
            break
        elif ganancias > 0:
            dinero += ganancias
            apuesta = dinero_minimo_apuesta
            dinero -= apuesta
        historial_dinero[i] = dinero

    dinero_final = dinero

    # if True:
    #     plt.plot(historial_dinero)
    #     plt.ylim([0,np.max(historial_dinero) + 10])
    #     plt.show()

    return dinero_final, se_ha_perdido, historial_dinero, historial_apuesta




# ---------------------------------------------------
# Evolución del dinero:
# ---------------------------------------------------

# Ejemplo 1
random.seed(124)

n_turnos = 100
dinero_inicial = 1000
dinero_minimo_apuesta = 1

fig, axs = plt.subplots(3, 5, figsize=(10, 7))
fig.suptitle(f'Evolución del dinero\n{n_turnos} turnos, dinero inicial = {dinero_inicial}, apuesta minima = {dinero_minimo_apuesta}', fontsize=16)

for i in range(3):
    for j in range(5):
        dinero_final, se_ha_perdido, historial_dinero, historial_apuesta = simulacion_turno(turnos = n_turnos, dinero_inicial= dinero_inicial, dinero_minimo_apuesta = dinero_minimo_apuesta)
        axs[i, j].plot(historial_dinero)
        axs[i,j].set_ylim([0, dinero_inicial + 100*dinero_minimo_apuesta])

plt.savefig(os.path.join(directorio_actual, "Imagenes", "Evolucion_dinero_ejemplo_1"))
plt.show()



# Ejemplo 2
random.seed(124)

n_turnos = 100
dinero_inicial = 1000
dinero_minimo_apuesta = 10

fig, axs = plt.subplots(3, 5, figsize=(10, 7))
fig.suptitle(f'Evolución del dinero\n{n_turnos} turnos, dinero inicial = {dinero_inicial}, apuesta minima = {dinero_minimo_apuesta}', fontsize=16)
for i in range(3):
    for j in range(5):
        dinero_final, se_ha_perdido, historial_dinero, historial_apuesta = simulacion_turno(turnos = n_turnos, dinero_inicial= dinero_inicial, dinero_minimo_apuesta = dinero_minimo_apuesta)
        axs[i, j].plot(historial_dinero)
        axs[i,j].set_ylim([0, dinero_inicial + 100*dinero_minimo_apuesta])

plt.savefig(os.path.join(directorio_actual, "Imagenes", "Evolucion_dinero_ejemplo_2"))
plt.show()




# ---------------------------------------------------
# Cantidad apostada por turno:
# ---------------------------------------------------


# Ejemplo 1
random.seed(124)

n_turnos = 100
dinero_inicial = 1000
dinero_minimo_apuesta = 1

fig, axs = plt.subplots(3, 5, figsize=(10, 7))
fig.suptitle(f'Dinero apostado en cada turno\n{n_turnos} turnos, dinero inicial = {dinero_inicial}, apuesta minima = {dinero_minimo_apuesta}', fontsize=16)

for i in range(3):
    for j in range(5):
        dinero_final, se_ha_perdido, historial_dinero, historial_apuesta = simulacion_turno(turnos = n_turnos, dinero_inicial= dinero_inicial, dinero_minimo_apuesta = dinero_minimo_apuesta)
        axs[i, j].plot(historial_apuesta)

plt.savefig(os.path.join(directorio_actual, "Imagenes", "Dinero_apostado_ejemplo_1"))
plt.show()



# Ejemplo 2
random.seed(124)

n_turnos = 100
dinero_inicial = 1000
dinero_minimo_apuesta = 10

fig, axs = plt.subplots(3, 5, figsize=(10, 7))
fig.suptitle(f'Dinero apostado en cada turno\n{n_turnos} turnos, dinero inicial = {dinero_inicial}, apuesta minima = {dinero_minimo_apuesta}', fontsize=16)
for i in range(3):
    for j in range(5):
        dinero_final, se_ha_perdido, historial_dinero, historial_apuesta = simulacion_turno(turnos = n_turnos, dinero_inicial= dinero_inicial, dinero_minimo_apuesta = dinero_minimo_apuesta)
        axs[i, j].plot(historial_apuesta)

plt.savefig(os.path.join(directorio_actual, "Imagenes", "Dinero_apostado_ejemplo_2"))
plt.show()



# ------------------------------------------------------
# Cantidad de victorias y derrotas y dinero medio final:
# ------------------------------------------------------
random.seed(124)


# Ejemplo 1
N = 100000
n_turnos = 100
dinero_inicial = 1000
dinero_minimo_apuesta = 1

h = {"Perdido":0, "Ganado": 0}
media = 0
for i in range(N):
    dinero_final, se_ha_perdido, historial_dinero, historial_apuesta = simulacion_turno(turnos = n_turnos, dinero_inicial= dinero_inicial, dinero_minimo_apuesta = dinero_minimo_apuesta)
    if se_ha_perdido:
        h["Perdido"] += 1
    else:
        h["Ganado"] += 1

    media += dinero_final

h["Perdido"] = h["Perdido"] / N
h["Ganado"] = h["Ganado"] / N
media = media / N
plt.bar(h.keys(), h.values())
plt.title(f'Frecuencia de victoria (no perder todo el dinero)\n{n_turnos} turnos, dinero inicial = {dinero_inicial}, apuesta minima = {dinero_minimo_apuesta}')
plt.savefig(os.path.join(directorio_actual, "Imagenes", "Frecuencia_de_victoria_ejemplo_1"))
plt.show()
print(media)



# Ejemplo 2
N = 100000
n_turnos = 100
dinero_inicial = 1000
dinero_minimo_apuesta = 10

h = {"Perdido":0, "Ganado": 0}
media = 0
for i in range(N):
    dinero_final, se_ha_perdido, historial_dinero, historial_apuesta = simulacion_turno(turnos = n_turnos, dinero_inicial= dinero_inicial, dinero_minimo_apuesta = dinero_minimo_apuesta)
    if se_ha_perdido:
        h["Perdido"] += 1
    else:
        h["Ganado"] += 1

    media += dinero_final

h["Perdido"] = h["Perdido"] / N
h["Ganado"] = h["Ganado"] / N
media = media / N
plt.bar(h.keys(), h.values())
plt.title(f'Frecuencia de victoria (no perder todo el dinero)\n{n_turnos} turnos, dinero inicial = {dinero_inicial}, apuesta minima = {dinero_minimo_apuesta}')
plt.savefig(os.path.join(directorio_actual, "Imagenes", "Frecuencia_de_victoria_ejemplo_2"))
plt.show()
print(media)



# --------------------------------------------
# Dinero medio final en base al dinero inicial
# --------------------------------------------
N = 100000
n_turnos = 100
dinero_minimo_apuesta = 10
dineros_iniciales = np.linspace(1000, 100000,100).tolist()

proporciones = np.zeros(100)
for i,dinero_inicial in  enumerate(dineros_iniciales):
    media = 0
    for _ in range(N):
        dinero_final, se_ha_perdido, historial_dinero, historial_apuesta = simulacion_turno(turnos = n_turnos, dinero_inicial= dinero_inicial, dinero_minimo_apuesta = dinero_minimo_apuesta)
        media += dinero_final
    media = media / N
    proporciones[i] = media / dinero_inicial

for i, dinero in enumerate(dineros_iniciales):
    dineros_iniciales[i] = str(dinero)

plt.bar(dineros_iniciales,proporciones)
plt.axhline(y=1, color='r', linestyle='--')
plt.xticks(range(len(dineros_iniciales)), [str(int(round(float(dinero))) // 1000) for dinero in dineros_iniciales], rotation=90)
plt.text(len(dineros_iniciales) + 8, 0.79, r"$\times 1000€$", ha='right', fontsize = 20)
plt.ylim([0.8,1.05])
plt.title(f"Proporción media del dinero que queda tras una ronda de {n_turnos} turnos\nApuesta mínima = {dinero_minimo_apuesta}")
plt.xlabel("Dinero inicial")
plt.savefig(os.path.join(directorio_actual, "Imagenes", "Proporción del dinero final para diferentes turnos de dinero inicial"))
plt.show()

prop_max = np.max(proporciones)
indice = np.argmax(proporciones)
dinero_inicial_propmax = dineros_iniciales[indice]
print(f"Proporción máxima: {prop_max}")
print(f"Dinero inicial para proporción máxima: {dinero_inicial_propmax}")




# -------------------------------------------------------
# Expected value (apostar 1$ y de media -0.053$ ganancia)
# -------------------------------------------------------
N_es = np.linspace(100,100000,1000, dtype= "int")
ganancias_medias = []
for N in N_es:
    ganancias = np.zeros(N)
    for i in range(N):
        ganancias[i] = ruleta.apostar(1) - 1
    ganancias_medias.append(np.mean(ganancias))

plt.plot(N_es, ganancias_medias)
plt.axhline(y=0, color='g', linestyle='--')
plt.axhline(y=-0.027, color='r', linestyle='--')
plt.xlabel("Cantidad de iteraciones")
plt.ylabel("Ganancia media")
plt.title("Ganancia media apostando 1€")
plt.savefig(os.path.join(directorio_actual, "Imagenes", "Ganancia_media_en_base_al_numero_iteraciones"))
plt.show()