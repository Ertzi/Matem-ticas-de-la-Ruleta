from clase_ruleta import Ruleta
import numpy as np
import matplotlib.pyplot as plt


T = 5000
N = 1000
apuestas_color = Ruleta("color")
historial = np.zeros(T)


for i in range(T):
    if N < 10:
        break
    N = N - 10
    apuesta = 10
    N += apuestas_color.apostar(apuesta, color = "negro")
    historial[i] = N

plt.plot(historial)
plt.ylim([0,np.max(historial) + 10])
plt.show()
