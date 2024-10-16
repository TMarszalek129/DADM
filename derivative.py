import numpy as np
import matplotlib.pyplot as plt

def detect_maxima(x, t, plot=False):
    dy = np.gradient(x, t)
    maxima_indices = np.where((dy[:-1] > 0) & (dy[1:] < 0))[0]
    maxima_x = x[maxima_indices]
    maxima_y = t[maxima_indices]

    # Filtruj maksima tak, aby pierwsze zawsze było brane, a kolejne tylko, gdy różnica czasu wynosi co najmniej 200 ms
    filtered_maxima_indices = [maxima_indices[0]]  # Zawsze bierzemy pierwsze maksimum
    last_max_time = t[maxima_indices[0]]  # Czas pierwszego maksimum

    for index in maxima_indices[1:]:
        current_time = t[index]
        if current_time - last_max_time >= 0.2:
            filtered_maxima_indices.append(index)
            last_max_time = current_time

    filtered_maxima_indices = np.array(filtered_maxima_indices)
    
    # Zwróć punkty x oraz y odpowiadające przefiltrowanym maksimom
    maxima_x_r = x[filtered_maxima_indices]
    maxima_y_r = t[filtered_maxima_indices]

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
        plt.scatter(maxima_y_r, maxima_x_r, color='g', label='Przefiltrowane maksima', zorder=5)
        plt.title("Wykryte maksima po filtracji (co najmniej 200 ms)")
        plt.xlabel("Czas [s]")
        plt.ylabel("Napięcie [V]")
        plt.legend()
        plt.grid(True)
        plt.show()

    return maxima_x_r, maxima_y_r

