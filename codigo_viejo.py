import random
import numpy as np
import matplotlib.pyplot as plt

# Supondremos que siempre vamos a apostar al mismo color: el color ROJO
# Los valores pares son color ROJO
# Los valores impares son color NEGRO

def ruleta():
    return random.randint(0,36)

total_partidas = 100

dinero_inicial = 1000
numero_de_tiradas = 100
dinero_minimo_entrada = 10



valores_de_apuesta = np.zeros(numero_de_tiradas)
historial_del_dinero = np.zeros(numero_de_tiradas)
historial_dinero_doblado = np.zeros(numero_de_tiradas)


# Empiezan los turnos:
historial_ganados = np.zeros(total_partidas)
for j in range(total_partidas):
    todo_el_dinero_perdido = False
    apuesta_maxima = 0
    doblar_dinero = 0       
    dinero_total = dinero_inicial # Dinero del jugador
    apuesta = dinero_minimo_entrada
    dinero_total = dinero_total - apuesta
    for i in range(numero_de_tiradas):
        valores_de_apuesta[i] = apuesta
        historial_del_dinero[i] = dinero_total
        historial_dinero_doblado[i] = doblar_dinero

        valor = ruleta()
        if not (valor == 0 or valor % 2 != 0):
            dinero_total = dinero_total +  2*apuesta - dinero_minimo_entrada
            apuesta = dinero_minimo_entrada
            doblar_dinero = 0
        elif (dinero_total - 2*apuesta >= 0):
            doblar_dinero += 1
            apuesta = 2* apuesta
            dinero_total = dinero_total - apuesta
        else:
            apuesta = 2* apuesta
            dinero_total = dinero_total - apuesta
            doblar_dinero += 1
            todo_el_dinero_perdido = True
            break

        if apuesta > apuesta_maxima:
            apuesta_maxima = apuesta
    historial_ganados[j] = todo_el_dinero_perdido

print(historial_ganados )



print("------------------ PARTIDA ------------------")
print(f"Dinero en total: {dinero_total}")
print(f"Apuesta máxima: {apuesta_maxima}")
print(f"He perdido todo el dinero? {todo_el_dinero_perdido}")
print("---------------------------------------------\n")

fig, axs = plt.subplots(1, 3, figsize=(13, 4))

# Gráfico 1: Valores de apuesta
axs[0].plot(valores_de_apuesta)
axs[0].set_title('Valores de Apuesta')

# Gráfico 2: Historial del dinero
axs[1].plot(historial_del_dinero)
axs[1].set_title('Historial del Dinero')
axs[1].set_ylim(0,dinero_inicial + dinero_minimo_entrada * numero_de_tiradas)


# Gráfico 3: Historial del dinero doblado
axs[2].plot(historial_dinero_doblado)
axs[2].set_title('Numero de veces dobladas')

# Ajustar espaciado entre subtramas
plt.tight_layout()

# Mostrar la figura
plt.show()

plt.hist(historial_ganados)
plt.show()





