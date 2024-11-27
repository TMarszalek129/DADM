import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def ransac(x_values, y_values, x, y, data, wave):

    X = np.array([np.ones(len(x_values)), x_values]).T
    Y = y_values.T

    betas = np.linalg.inv(X.T @ X) @ X.T @ Y
    yn = np.array([np.ones(len(x)), x]).T @ betas

    thr = 0.2
    y_min = yn - thr * np.mean(yn)
    y_max = yn + thr * np.mean(yn)

    good_indices = []
    for i in range(len(y)):
        min_val = y_min[i]
        max_val = y_max[i]
        if y[i] > min_val and y[i] < max_val:
            good_indices.append(i)

    print('Good indices is ', len(good_indices) / len(y) * 100, '%')

    X = np.array([np.ones(len(good_indices)),x[good_indices]]).T
    Y = np.array(y[good_indices]).T

    betas = np.linalg.inv(X.T @ X) @ X.T @ Y
    yn_good = np.array([np.ones(len(x[good_indices])), x[good_indices]]).T @ betas

    if wave:
        plt.figure()
        plt.plot(data[0, :],data[1, :], 'r*', label='Dane')
        plt.plot(x_values, y_values, 'ko')
        plt.plot(x, yn, 'g-', label='Dopasowana prosta dla 2 punktów')
        plt.plot(x, y_min, 'b-', label='Zakresy')
        plt.plot(x, y_max, 'b-')
        plt.plot(x[good_indices], yn_good, 'k-', label='Dopasowana prosta dla wszystkich danych')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Dopasowanie prostej metodą RANSAC')
        plt.legend()
        plt.grid()
        plt.show()

def ols(x, y, wave):

    X = np.vstack((x, np.ones(len(x)))).T
    beta, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    slope, intercept = beta

    if wave:
        plt.scatter(x, y, label='Dane')
        plt.plot(x, slope * x + intercept, color='red', label='Dopasowana prosta')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Dopasowanie prostej metodą OLS')
        plt.legend()
        plt.grid()
        plt.show()


def ransac_eng(max, min, x, y, wave):
    results = []
    beta = []
    l_max = []
    l_min = []
    indi = []

    for j in range(len(max)):
        X_eng = np.array([np.ones(len(x[max[j]:min[j]])), x[max[j]:min[j]]]).T
        Y_eng = y[max[j]:min[j]]

        betas_eng = np.linalg.inv(X_eng.T @ X_eng) @ X_eng.T @ Y_eng
        yn = X_eng @ betas_eng

        results.append(yn)
        beta.append(betas_eng[0][0])

        thr = 0.2
        y_min = yn - thr * np.mean(yn)
        y_max = yn + thr * np.mean(yn)

        l_max.append(y_max)
        l_min.append(y_min)

        indi.append(x[max[j]:min[j]])

    if wave:
        plt.figure()
        plt.plot(x, y, 'r')
        for i in range(len(results)):
            plt.plot(indi[i], l_min[i], 'b-')
            plt.plot(indi[i], l_max[i], 'b-')
            plt.plot(indi[i], results[i], 'k-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Dopasowanie prostej metodą RANSAC')
        plt.grid()
        plt.show()
    return beta

def ols_eng(max, min, x, y, wave):
    results = []
    betas = []
    indi = []

    for j in range(len(max)):
        X = np.vstack((x[max[j]:min[j]], np.ones(len(x[max[j]:min[j]])))).T
        beta, _, _, _ = np.linalg.lstsq(X, y[max[j]:min[j]], rcond=None)
        slope, intercept = beta
        indi.append(x[max[j]:min[j]])
        results.append(slope * x[max[j]:min[j]] + intercept)
        betas.append(slope[0])

    if wave:
        plt.plot(x, y, 'r')
        for i in range(len(results)):
            plt.plot(indi[i], results[i], 'k-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Dopasowanie prostej metodą OLS')
        plt.grid()
        plt.show()
    return betas

def detect_extrema(signal, time, plot_flag):
    # Wykrywanie maksimów
    maxima, _ = find_peaks(signal, height=5, distance=80)
    
    # Wykrywanie minimów (przez odwrócenie sygnału)
    minima, _ = find_peaks(-signal, height=5, distance=95)
    
    # Jeśli plot_flag jest True, wyświetl wykres
    if plot_flag:
        plt.figure(figsize=(10, 6))
        plt.plot(time, signal, label='Sygnał', color='blue')  # Rysowanie sygnału
        plt.scatter(time[maxima], signal[maxima], color='red', label='Maksima', zorder=5)  # Rysowanie maksimów
        plt.scatter(time[minima], signal[minima], color='green', label='Minima', zorder=5)  # Rysowanie minimów
        plt.title('Wykrywanie maksimów i minimów sygnału')
        plt.xlabel('Czas')
        plt.ylabel('Wartość sygnału')
        plt.legend()
        plt.grid(True)
        plt.show()

    return maxima, minima
