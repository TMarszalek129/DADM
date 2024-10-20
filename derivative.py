import numpy as np
import matplotlib.pyplot as plt

def detect_maxima(x, t, plot=False):
    dy = np.gradient(x, t)
    maxima_indices = np.where((dy[:-1] > 0) & (dy[1:] < 0))[0]
    maxima_x = x[maxima_indices]
    maxima_y = t[maxima_indices]

    if plot:
        # Wykres oryginalnego sygnału
        plt.figure()
        plt.plot(t, x, label='Sygnał EKG', color='b')
        plt.scatter(maxima_y, maxima_x, color='r', label='Wszystkie maksima', zorder=5)
        plt.title("Wykryte maksima na sygnale")
        plt.xlabel("Czas [s]")
        plt.ylabel("Napięcie [V]")
        plt.legend()
        plt.grid(True)
        plt.show()

        # Wykres z przefiltrowanymi maksimami
        plt.figure()
        plt.plot(t, x, label='Sygnał EKG', color='b')
        plt.scatter(maxima_y, maxima_x, color='g', label='Przefiltrowane maksima', zorder=5)
        plt.title("Wykryte maksima po filtracji (co najmniej 200 ms)")
        plt.xlabel("Czas [s]")
        plt.ylabel("Napięcie [V]")
        plt.legend()
        plt.grid(True)
        plt.show()

    return maxima_y, maxima_x

