from clase_ruleta import Ruleta
import numpy as np
import matplotlib.pyplot as plt

ruleta = Ruleta()

def hay_dinero_suficiento(dinero,apuesta):
    return dinero >= apuesta

def simulacion_turnos(turnos, dinero_inicial, dinero_minimo_apuesta, graficar = True):
    se_ha_perdido = False
    historial_dinero = np.zeros(turnos)
    dinero = dinero_inicial # Dinero al inicio 
    historial_dinero[0] = dinero

    # Apostar:
    apuesta = dinero_minimo_apuesta
    dinero -= apuesta

    for i in range(1, turnos):
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

    if graficar:
        plt.plot(historial_dinero)
        plt.ylim([0,np.max(historial_dinero) + 10])
        plt.show()

    return dinero, se_ha_perdido



# simulacion_turnos(100,1000,10,True)


dinero_banco = 1000000
numero_de_accesos_casino = 50
hist_dinero = np.zeros(numero_de_accesos_casino)
for i in range(numero_de_accesos_casino):
    if dinero_banco >= 1000:
        dinero_turno = 10000
        dinero_banco-= dinero_turno
        dinero, se_ha_perdido = simulacion_turnos(100, dinero_turno, 10, False)
        dinero_banco += dinero
    else:
        print("Se ha perdido el dinero")
        hist_dinero[i:] = dinero_banco
        break
    hist_dinero[i] = dinero_banco

plt.plot(hist_dinero)
plt.ylim([np.min(hist_dinero)-10,np.max(hist_dinero) + 10])
plt.show()

