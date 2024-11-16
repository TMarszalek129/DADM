import numpy as np
def fluct_mean(y, y_n):
    F = []

    for j in range(len(y)):
        N = len(y[j][0]) * len(y[j][1])
        F.append(np.sqrt(1/N) * np.sum((y[j] - y_n[j]))**2)

    F = np.array(F)

    return F
