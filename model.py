import numpy as np
import matplotlib.pyplot as plt

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

def ols(x, y, data, wave):

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
