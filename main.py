import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from model import ransac, ols, ransac_eng, ols_eng, detect_extrema

OPERATIONS = ['real']

if 'synthetic' in OPERATIONS:
    path = '../../data1.mat'
    # path = 'C:/Users/bartl/Downloads/data1.mat'

    data = loadmat(path)
    data = data['data1']

    x = data[0, :]
    y = data[1, :]

    x_ransac, yn_ransac = ransac(x, y, True)
    x_ols, yn_ols = ols(x, y, True)

    plt.figure()
    plt.plot(x, y, 'r*', label='Data')
    plt.plot(x_ransac, yn_ransac, 'b-', label='Fitted line using RANSAC method')
    plt.plot(x_ols, yn_ols, 'g-', label='Fitted line using OLS method')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('The comparison of fitted lines using various methods')
    plt.legend()
    plt.grid()
    plt.show()


if 'real' in OPERATIONS:
    # path_eng = 'C:/Users/bartl/Downloads/eng_signals.mat'
    path_eng = '../../eng_signals.mat'

    data_eng = loadmat(path_eng)
    data_eng = data_eng['eng_signal1']

    f_p = 100
    t = np.arange(0, len(data_eng) / f_p, 1 / f_p)

    max, min = detect_extrema(data_eng.ravel(), t, False)
    max, min = max[:-1], min[1:]
    # v_ransac = ransac_eng(max[:-1], min[1:], t, data_eng, True)
    betas_rans, good_ind_rans, y_rans = ransac_eng(max, min, t, data_eng, False)
    betas_ols, good_ins_ols, y_ols = ols_eng(max, min, t, data_eng, False)

    plt.figure()
    plt.plot(t, data_eng, 'r-')
    for i in range(len(y_rans)):
        plt.plot(t[good_ind_rans[i]], y_rans[i], 'b-')
        plt.plot(t[good_ins_ols[i]], y_ols[i], 'g-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('The comparison of fitted lines using various methods')
    plt.legend(['Data', 'RANSAC', 'OLS'])
    plt.grid()
    plt.xlim([5, 8])
    plt.show()

    # print(f"Średnia prękość fazy wolnej [RANSAC]: {np.mean(v_ransac):.2f}, Odchylenie standardowe fazy wolnej [RANSAC]: {np.std(v_ransac):.2f}")
    # print(f"Średnia prękość fazy wolnej [OLS]: {np.mean(v_ols):.2f}, Odchylenie standardowe fazy wolnej [OLS]: {np.std(v_ols):.2f}")

    arr_grad_rans, arr_grad_ols = [], []
    for i in range(len(y_rans)):
        rans_grad = y_rans[i][-1] - y_rans[i][-1] / t[good_ind_rans[i][-1]] - t[good_ind_rans[i][0]]
        ols_grad = y_ols[i][-1] - y_ols[i][-1] / t[good_ins_ols[i][-1]] - t[good_ins_ols[i][0]]

        arr_grad_rans.append(rans_grad)
        arr_grad_ols.append(ols_grad)

    v_mean_rans, v_mean_ols = np.mean(arr_grad_rans), np.mean(arr_grad_ols)
    v_std_rans, v_std_ols = np.std(arr_grad_rans), np.std(arr_grad_ols)