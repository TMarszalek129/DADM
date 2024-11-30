import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def ransac(x, y, wave):

    while(True):
        indices = np.arange(len(x))
        samples = np.random.choice(indices, 2)
        x_values = x[samples]
        y_values = y[samples]

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

        good_percent = len(good_indices) / len(y) * 100


        if(good_percent > 70):
            print('Good indices is ', good_percent, '%')
            break
        print('Good indices is ', good_percent, '% - level is too low')

    X = np.array([np.ones(len(good_indices)),x[good_indices]]).T
    Y = np.array(y[good_indices]).T

    betas = np.linalg.inv(X.T @ X) @ X.T @ Y
    yn_good = np.array([np.ones(len(x[good_indices])), x[good_indices]]).T @ betas

    if wave:
        plt.figure()
        plt.plot(x, y, 'r*', label='Data')
        plt.plot(x_values, y_values, 'ko')
        plt.plot(x, yn, 'g-', label='Fitted line for 2 points')
        plt.plot(x, y_min, 'b-', label='Ranges')
        plt.plot(x, y_max, 'b-')
        plt.plot(x[good_indices], yn_good, 'k-', label='Fitted line for all points')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Fitted line using the RANSAC method')
        plt.legend()
        plt.grid()
        plt.show()

    return x[good_indices], yn_good

def ransac_eng(max, min, x, y, wave):
    yn_eng = []
    betas_eng = []
    y_max_eng = []
    y_min_eng = []
    indices = []
    good_indices_eng = []


    for j in range(len(max)):
        print(j, ' phase, min value: ', min[j], ', max value: ', max[j])
        counter = 0
        while(True):
            x_j = x[max[j]:min[j]]
            y_j = y[max[j]:min[j]]

            indices_j = np.arange(max[j], min[j]) - max[j]
            samples = np.random.choice(indices_j, 2)
            x_values = x_j[samples]
            y_values = y_j[samples]

            X_j = np.array([np.ones(len(x_values)), x_values]).T
            Y_j = y_values


            betas_j = np.linalg.inv(X_j.T @ X_j) @ X_j.T @ Y_j
            yn = np.array([np.ones(len(x_j)), x_j]).T @ betas_j
            thr = 0.5
            mean = np.mean(yn)
            if(mean > 0):
                y_min = yn - thr * np.mean(yn)
                y_max = yn + thr * np.mean(yn)
            else:
                y_min = yn + thr * np.mean(yn)
                y_max = yn - thr * np.mean(yn)

            good_indices = []
            for i in range(len(y_j)):
                min_val = y_min[i]
                max_val = y_max[i]
                if y_j[i] > min_val and y_j[i] < max_val:
                    good_indices.append(i)

            good_percent = len(good_indices) / len(y_j) * 100
            thr = 70 - (counter // 2)
            print('Threshold level: ', thr, ' %')
            if (good_percent >= thr):
                print('Good indices is ', good_percent, '%')
                break
            print('Good indices is ', good_percent, '% - level is too low')
            counter = counter + 1
        X = np.array([np.ones(len(good_indices)), x_j[good_indices]]).T
        Y = np.array(y_j[good_indices])

        betas = np.linalg.inv(X.T @ X) @ X.T @ Y
        yn_good = X @ betas

        yn_eng.append(yn_good)
        betas_eng.append(betas_j)
        y_max_eng.append(y_max)
        y_min_eng.append(y_min)
        indices.append(np.arange(max[j], min[j]))
        good_indices_eng.append(good_indices + max[j])


    if wave:
        plt.figure()
        plt.plot(x, y, 'r-')
        for i in range(len(yn_eng)):
            plt.plot(x[good_indices_eng[i]], yn_eng[i], 'k-', label='Fitted line')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Fitted line using RANSAC method')
        plt.grid()
        # plt.xlim([3, 8])
        plt.show()
    return betas, good_indices_eng, yn_eng

def ols(x, y, wave):

    X = np.array([np.ones(len(x)), x]).T
    Y = y.T

    betas = np.linalg.inv(X.T @ X) @ X.T @ y
    yn = X @ betas

    if wave:
        plt.plot(x, y, 'r*', label='Data')
        plt.plot(x, yn, 'b-', label='Fitted line')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Fitted line using the OLS method')
        plt.legend()
        plt.grid()
        plt.show()

    return x, yn

def ols_eng(max, min, x, y, wave):
    results_arr = []
    betas_arr = []
    indi_arr = []

    for j in range(len(max)):

        X = np.array([np.ones(len(x[max[j]:min[j]])), x[max[j]:min[j]]]).T
        Y = np.array(y[max[j]:min[j]])

        betas = np.linalg.inv(X.T @ X) @ X.T @ Y
        yn = X @ betas
        indi_arr.append(np.arange(max[j], min[j]))
        results_arr.append(yn)
        betas_arr.append(betas)

    if wave:
        plt.plot(x, y, 'r')
        for i in range(len(results_arr)):
            plt.plot(x[indi_arr[i]], results_arr[i], 'k-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Fitted line using OLS method')
        plt.grid()
        plt.show()
    return betas, indi_arr, results_arr

def detect_extrema(signal, time, plot_flag):

    maxima, _ = find_peaks(signal, height=5, distance=80)
    minima, _ = find_peaks(-signal, height=5, distance=95)

    if plot_flag:
        plt.figure(figsize=(10, 6))
        plt.plot(time, signal, label='Signal', color='blue')
        plt.scatter(time[maxima], signal[maxima], color='red', label='Maximums', zorder=5)
        plt.scatter(time[minima], signal[minima], color='green', label='Minimums', zorder=5)
        plt.title('Detected maximums and minimums')
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        plt.legend()
        plt.grid(True)
        plt.show()

    return maxima, minima
